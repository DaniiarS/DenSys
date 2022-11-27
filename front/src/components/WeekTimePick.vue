<template>
    <div class="vdpComponent" :class="{vdpWithInput: hasInputElement}">
        <input
            class="w-full relative border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring ease-linear transition-all duration-150 disabled:text-slate-300"
            type="text"
            :readonly="isReadOnly"
            :value="TotalHours + ' hours a week'"
            @focus="editable && open()"
            @click="editable && open()">

        <transition name="vdp-toggle-calendar">
        <div
            v-if="opened"
            class="vdpOuterWrap"
            ref="outerWrap"
            @click="closeViaOverlay"
            :class="[positionClass, {vdpFloating: hasInputElement}]">
            <div class="vdpInnerWrap">
                <header class="vdpHeader">
                </header>
                <table class="vdpTable">
                <thead>
                <tr>
                <th class="wtpHeadCell" v-for="(weekday, weekdayIndex) in weekdays" :key="weekdayIndex">
                    <span class="text-slate-400 text-sm">{{weekday}}</span>
                </th>
                </tr>
                </thead>

                <tbody :class="directionClass">
                <tr class="vdpRow" v-for="(a,nor) in NumberOfRows" :key="nor">
                <td class="wtpCell" v-for="(timeslot, tsidx) in value" :key="tsidx" >
                    <div v-show="timeslot[nor]"  class="text-xs text-slate-600">
                         {{timeslot[nor]}}
                        <button class="inline-block fa-solid fa-minus text-rose-500    hover:text-rose-600"
                                @click="RemoveTimeSlot(nor, tsidx)"
                                ></button>
                    </div>
                    <div v-show="!timeslot[nor] && (nor==0 || timeslot[nor-1])" class="text-xs text-slate-600">
                        <button class="fa-solid fa-plus" v-show="tsidx != timeSlotAt" @click="NewTimeSlot(tsidx)"></button>
                        <input v-model="new_timeslot" class="border-2 w-full text-center" v-show="tsidx == timeSlotAt"/>
                        <button v-show="tsidx == timeSlotAt"
                                class="px-4 fa-solid fa-check text-emerald-500 hover:text-emerald-600"
                                @click="AddTimeSlot"
                                ></button>
                        <button v-show="tsidx == timeSlotAt"
                                class="px-4 fa-solid fa-xmark text-rose-500    hover:text-rose-600"
                                @click="NoAddTimeSlot"
                                ></button>
                    </div>
                </td>
                </tr>
                </tbody>
                </table>
            </div>
        </div>
        </transition>
    </div>
</template>

<script>
import "@/vueDatePick.css"
import "@/output.css"
//import TimeSelector from "@/components/VueTimeSelector.vue"

export default {

    props: {
        value: {
            type: Array,
            default: () => [[],[],[],[],[],[],[]]
        },
        isReadOnly: {
            type: Boolean,
            default: true
        },
        hasInputElement: {
            type: Boolean,
            default: true
        },
        weekdays: {
            type: Array,
            default: () => ([
                'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'
            ])
        },
        editable: {
            type:    Boolean,
            default: true
        },
        mobileBreakpointWidth: {
            type: Number,
            default: 500
        },
    },
    components: {
        //TimeSelector,
    },
    computed: {
        // a computed getter
        NumberOfRows() {
            var max = 0
            for (const ts of this.value) {
                if (ts.length > max) {
                    max = ts.length
                }
            }
            return max+1
        },
        TotalHours() {
            var totalHours = 0
            for (const timeslots of this.value) {
                for (const ts of timeslots) {
                    // 00:00 - 10:00
                    // 0123456789012
                    const hs = ts[0]*10+(+ts[1])
                    const ms = ts[3]*10+(+ts[4])
                    const he = ts[8]*10+(+ts[9])
                    const me = ts[11]*10+(+ts[12])
                    totalHours += (he-hs) + (me-ms)/60
                }
            }
            totalHours = Math.round(totalHours)
            return totalHours
        },
    },

    data() {
        return {
            positionClass: undefined,
            direction:     undefined,
            timeSlotAt:   undefined,
            new_timeslot: undefined,
            opened:       false,
        };
    },
    beforeUnmount() {
        this.removeCloseEvents()
        this.teardownPosition()
    },

    methods: {
        CopyArray(arr) {
            return JSON.parse(JSON.stringify(arr))
        },
        NewTimeSlot(idx) {
            this.timeSlotAt = idx
        },
        RemoveTimeSlot(ridx, tsidx) {
            var weekTimeSlots = this.CopyArray(this.value)
            weekTimeSlots[tsidx].splice(ridx, 1)
            this.$emit('update:value', weekTimeSlots);
            this.new_timeslot = undefined
            this.timeSlotAt   = undefined
        },
        AddTimeSlot() {
            if (this.new_timeslot) {
                var weekTimeSlots = this.CopyArray(this.value)
                weekTimeSlots[this.timeSlotAt].push(this.new_timeslot)
                this.$emit('update:value', weekTimeSlots);
                this.new_timeslot = undefined
                this.timeSlotAt   = undefined
            }
        },
        NoAddTimeSlot() {
            this.new_timeslot = undefined
            this.timeSlotAt   = undefined
        },
        directionClass() {
            return this.direction ? `vdp${this.direction}Direction` : undefined;
        },
        open() {
            if (!this.opened) {
                this.opened = true;
                this.addCloseEvents();
                this.setupPosition();
            }
            this.direction = undefined;
        },
        close() {
            if (this.opened) {
                this.opened = false;
                this.direction = undefined;
                this.removeCloseEvents();
                this.teardownPosition();
            }

        },
        toggle() {
            return this.opened ? this.close() : this.open();
        },
        closeViaOverlay(e) {
            if (this.hasInputElement && e.target === this.$refs.outerWrap) {
                console.log("overlay close")
                this.close();
            }
        },
        setupPosition() {

            if (!this.positionEventListener) {
                this.positionEventListener = () => this.positionFloater();
                window.addEventListener('resize', this.positionEventListener);
            }

            this.positionFloater();

        },
        positionFloater() {

            const inputRect = this.$el.getBoundingClientRect();

            let verticalClass = 'vdpPositionTop';
            let horizontalClass = 'vdpPositionLeft';

            const calculate = () => {

                const rect = this.$refs.outerWrap.getBoundingClientRect();
                const floaterHeight = rect.height;
                const floaterWidth = rect.width;

                if (window.innerWidth > this.mobileBreakpointWidth) {

                    // vertical
                    if (
                        (inputRect.top + inputRect.height + floaterHeight > window.innerHeight) &&
                        (inputRect.top - floaterHeight > 0)
                    ) {
                        verticalClass = 'vdpPositionBottom';
                    }

                    // horizontal
                    if (inputRect.left + floaterWidth > window.innerWidth) {
                        horizontalClass = 'vdpPositionRight';
                    }

                    this.positionClass = ['vdpPositionReady', verticalClass, horizontalClass].join(' ');

                } else {

                    this.positionClass = 'vdpPositionFixed';

                }

            };

            this.$refs.outerWrap ? calculate() : this.$nextTick(calculate);

        },
        teardownPosition() {

            if (this.positionEventListener) {
                this.positionClass = undefined;
                window.removeEventListener('resize', this.positionEventListener);
                delete this.positionEventListener;
            }

        },

        clear() {

            this.$emit('update:value', '');

        },
        addCloseEvents() {

            if (!this.closeEventListener) {

                this.closeEventListener = e => this.inspectCloseEvent(e);

                ['click', 'keyup', 'focusin'].forEach(
                    eventName => document.addEventListener(eventName, this.closeEventListener)
                );

            }

        },

        inspectCloseEvent(event) {
            if (event.keyCode) {
                event.keyCode === 27 && this.close();
            }
            else if (!(event.target === this.$el) && !this.$el.contains(event.target)) {
                console.log("inspect close")
                this.close();
            }
        },

        removeCloseEvents() {

            if (this.closeEventListener) {

                ['click', 'keyup', 'focusin'].forEach(
                    eventName => document.removeEventListener(eventName, this.closeEventListener)
                );

                delete this.closeEventListener;

            }

        },
    },
};
</script>
