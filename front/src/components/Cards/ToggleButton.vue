<template>
  <button class="inline-block px-6 py-2.5
                 border-2 border-emerald-500
                 font-medium text-xs leading-tight uppercase
                 hover:text-white hover:bg-emerald-600
                 focus:bg-emerald-600 focus:text-white focus:outline-none focus:ring-0
                 active:bg-emerald-700 transition duration-150 ease-in-out"
          :class="[this.active_type === this.toggleButtonName ? 'bg-emerald-500 text-white' : 'bg-white text-emerald-500']"
          type="button"
          @click="updateActive">
    {{toggleButtonName}}
    </button>
</template>

<script>
export default {
  name: "toggle-button",

  props: ['active_type', 'toggleButtonName'],
  model: {
    prop: 'active_type',
    event: 'update:active_type'
  },

  methods: {
    updateActive() {
      this.$emit('update:active_type', this.toggleButtonName)
    }
  }
};
</script>
