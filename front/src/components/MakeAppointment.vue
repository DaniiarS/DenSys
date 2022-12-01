<template>
  <div class="container mx-auto flex content-center items-center justify-center h-full w-full">
    <div class="relative flex min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-slate-200 border-0">
      <div class="flex-auto px-4 lg:px-10 py-10 pt-0">
        <div class="text-slate-800 text-center py-3 font-bold">
          Doctor Appointment
        </div>
        <hr class="pb-4 border-t-1 border-slate-300" />
        <div class="flex-wrap">
          <div class="w-full px-4 inline-block relative mb-3">
            <div class="flex-wrap block uppercase text-slate-600 text-xs font-bold mb-2">
              Specialization <div class="inline-block text-rose-700 fa-2xs fa-solid fa-circle"></div>
            </div>
            <radio-form :buttons="['General','Pediatrist', 'Surgeon', 'Oculist', 'Neurologist']" v-model:input_type="specialization" @click="UpdateDoctors"/>
          </div>
          <div class="w-full px-4 inline-block relative">
            <div class="flex-wrap block uppercase text-slate-600 text-xs font-bold mb-2">
              Doctor <div class="inline-block text-rose-700 fa-2xs fa-solid fa-circle"></div>
            </div>
          </div>
          <div class="flex flex-wrap item-center">
            <doctor-card v-for="doctor in doctors_iins" :key="doctor.iin" :doctor_iin="doctor.iin"
              @click="ChooseDoctor(doctor.iin)" :isActive="doctor.iin == chosen_iin"/>
          </div>

          <div v-if="doctors_iins.length > 0" class="flex flex-nowrap px-4">
          <button class="flex-auto relative rounded transparent hover:shadow-lg py-3 w-3/12 fas fa-caret-left  fa-xl" @click="DecrementPage"></button>
          <div class="flex-none inline-block w-min-content">
            <button class="px-1 far fa-circle" :class="page == p ? 'fas' : ''" @click="UpdatePage(p)" v-for="(_, p) in pages" :key="p">
            </button>
          </div>
          <button class="flex-auto relative rounded transparent hover:shadow-lg py-3 w-3/12 fas fa-caret-right fa-xl" @click="IncrementPage"></button>
          </div>

          <div v-if="chosen_iin" class="w-full px-4 inline-block relative mb-3">
            <div class="flex-wrap block uppercase text-slate-600 text-xs font-bold mb-2">
              Time <div class="inline-block text-rose-700 fa-2xs fa-solid fa-circle"></div>
            </div>
            <div v-if="doctors_iins.length > 0" >
              <div class="flex flex-nowrap">
              <button class="flex-auto relative rounded transparent hover:shadow-lg py-3 w-3/12 fas fa-caret-left  fa-xl" @click="PrevWeek"></button>
              <div class="flex-none inline-block w-min-content">
                <div class="px-2">
                  December 2022
                </div>
              </div>
              <button class="flex-auto relative rounded transparent hover:shadow-lg py-3 w-3/12 fas fa-caret-right fa-xl" @click="NextWeek"></button>
              </div>

              <table class="w-full">
                <thead>
                  <tr class="bg-slate-100">
                    <th class="" v-for="(weekday, weekdayIndex) in weekdays" :key="weekdayIndex">
                      <div class="text-slate-400 text-sm">{{weekday}}</div>
                    </th>
                  </tr>
                </thead>

                <tbody class="">
                  <tr class="">
                    <td class="text-center align-middle" v-for="(week, didx) in week_schedules[weekat]" :key="didx" >
                      <button class="rounded-full w-8 h-8"
                              :class="dateat === didx
                                        ? 'bg-emerald-500 text-slate-200'
                                        : ''"
                              @click="dateat=didx; timeat=undefined">{{week.date}}</button>
                    </td>
                  </tr>
                </tbody>
              </table>

            <button class="rounded-full px-1 mx-1
                                  leading-tight uppercase
                                  border-2 border-slate-600
                                  shadow-lg
                                  transition duration-150 ease-in-out"
                    :class="timeat==time
                                        ? 'shadow border-emerald-500 text-emerald-500'
                                        : 'hover:shadow hover:border-slate-500 hover:text-slate-500 text-slate-600' "
                    v-for="(time,tidx) in week_schedules[weekat][dateat].times" :key="tidx" @click="timeat=time">{{time}}</button>
            <div v-if="week_schedules[weekat][dateat].times.length == 0">No time</div>
          </div>
          </div>

          <div class="text-center px-4 mt-6" >
            <button class="bg-slate-800 text-white
                               active:bg-slate-600
                               text-sm font-bold uppercase
                               px-6 py-3 rounded mr-1 mb-1 w-full
                               shadow hover:shadow-lg
                               outline-none focus:outline-none
                               ease-linear transition-all duration-150"
                    @click="SendAppointment"
                    type="button">
              Make An Appointment
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import axios from 'axios'
import {server_url} from '@/api.js'

import RadioForm  from "@/components/RadioForm.vue"
import DoctorCard from '@/components/DoctorCard.vue';


export default {
  data() {
    return {
      specialization:'',

      patient_iin: localStorage.getItem('user_iin'),
      doctors_iins:  [],
      chosen_iin:   '',

      week_schedules: [
        [
          { date: '28', times: ['00:00', '00:15'], },
          { date: '29', times: ['00:00', '00:15'], },
          { date: '30', times: ['00:00', '00:30', '00:45'], },
          { date: '1', times: ['00:00', '00:15'], },
          { date: '2', times: ['00:00', '00:15', '00:30'], },
          { date: '3', times: ['00:00', '00:15'], },
          { date: '4', times: ['00:00', '00:30'], },
        ],
        [
          { date: '5', times: ['00:00', '00:15'], },
          { date: '6', times: ['00:00', '00:15'], },
          { date: '7', times: ['00:00', '00:30', '00:45'], },
          { date: '9', times: ['00:00', '00:15'], },
          { date: '10', times: ['00:00', '00:15', '00:30'], },
          { date: '11', times: ['00:00', '00:15'], },
          { date: '12', times: ['00:00', '00:30'], },
        ],
      ],
      weekdays:['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],

      weekat: 0,
      dateat: 0,
      timeat: undefined,


      limit:  2,
      pages : 0,
      page  : 0,
    };
  },
  components: {
    //ToggleButton,
    RadioForm,
    DoctorCard,
    //DatePick,
  },
  methods: {
    ChooseDoctor(iin) {
      this.chosen_iin = iin
      this.weekat=0
      this.dateat=0
      this.timeat=undefined
      axios
        .get(`${server_url}/api/doctor/schedule/${this.chosen_iin}/`, { headers: {"Authorization": 'Token ' + localStorage.access_token} })
        .then((response) => {
          console.log(this.week_schedules)
          this.week_schedules = response.data.message
          console.log(this.week_schedules)
        })
        .catch(function (error) {
          alert("Could not Time")
          console.log(error)
        })

    },
    PrevWeek() {
      this.dateat = 0
      this.timeat = undefined
      this.weekat -=1
      if (this.weekat < 0) {
        this.weekat = 0
      }
    },
    NextWeek() {
      this.dateat = 0
      this.timeat = undefined
      this.weekat +=1
      if (this.weekat > 1) {
        this.weekat = 1
      }
    },
    UpdatePage(p) {
      this.page = p
      this.UpdateDoctors()
    },
    IncrementPage() {
      this.page += 1
      if (this.page >= this.pages) {
        this.page -=1
      }
      this.UpdateDoctors()
    },
    DecrementPage() {
      this.page -= 1
      if (this.page < 0) {
        this.page = 0
      }
      this.UpdateDoctors()
    },
    UpdateDoctors() {
      this.chosen_iin = ''
      if (!this.specialization) {
        this.doctors_iins = []
      }
      axios
        .get(`${server_url}/api/doctors/${this.specialization}/${this.limit}/${this.limit*this.page}/`, { headers: {"Authorization": 'Token ' + localStorage.access_token} })
        .then((response) => {
          console.log(response.data)
          this.doctors_iins = response.data.doctors
          this.pages        = Math.round(response.data.count/this.limit+0.5)
        })
        .catch(function (error) {
          alert("Could not load Doctor")
          console.log(error)
        })
    },
    SendAppointment() {
      console.log("token: " + localStorage.access_token)
      axios
        .post(`${server_url}/api/appointment/${this.patient_iin}/${this.chosen_iin}/${this.weekat}/${this.dateat}/${this.timeat}/`, { headers: {"Authorization": 'Token ' + localStorage.access_token} })
        .then((response) => {
          console.log(response.data)
          alert("Success")
        })
        .catch(function (error) {
          alert("Could not make appointment")
          console.log(error)
        })
    },
  }
};
</script>
