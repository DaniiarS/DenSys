<template>
    <div class="container mx-auto flex content-center items-center justify-center h-full w-full">
      <div class="relative break-words w-full mb-6 shadow-lg rounded-lg bg-slate-200 border-0">
        <div class="flex-auto px-4 lg:px-10 py-10 pt-0">
          <div class="text-slate-800 text-center py-3 font-bold">
            Service Request
          </div>
          <hr class="pb-4 border-t-1 border-slate-300" />
          <div class="flex-wrap">
            <div class="w-full px-4 inline-block relative mb-3">
              <div class="flex-wrap block uppercase text-slate-600 text-xs font-bold mb-2">
                Department <div class="inline-block text-rose-700 fa-2xs fa-solid fa-circle"></div>
              </div>

              <radio-form :buttons="['Surgery','Gynecology', 'Obstetrics', 'Pediatrics', 'Radiology', 'Eye', 'ENT', 'Dental', 'Orthopedics', 'Neurology', 'Cardiology', 'Psychiatry', 'Skin']"
                          v-model:input_type="department"
                          @click="UpdateDepartment"
              />
            </div>
            <div v-if="department" class="relative w-full break-words px-4 inline-block">
              <div class="flex-wrap block uppercase text-slate-600 text-xs font-bold mb-2">
                Service <div class="inline-block text-rose-700 fa-2xs fa-solid fa-circle"></div>
              </div>
              <div class="block w-full overflow-x-auto">
              <table class="items-center w-full border-collapse">
                <thead>
                  <tr class="align-middle border border-solid text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-center text-slate-200 bg-slate-800 border-slate-100">
                    <th class="px-1 lg:px-6 py-3">
                      Name
                    </th>
                    <th class="px-1 lg:px-6 py-3">
                      Department
                    </th>
                    <th class="px-1 lg:px-6 py-3">
                      Service Duration
                    </th>
                    <th class="px-1 lg:px-6 py-3">
                      Service Price
                    </th>
                  </tr>
                </thead>
                <tbody>
                  <tr class="
                             text-xs text-center align-middle whitespace-nowrap
                             hover:text-slate-100 hover:bg-emerald-600
                             active:bg-emerald-500 transition duration-150 ease-in-out
                             border-t-1 border-solid border-slate-200 border-l-0 border-r-0"
                      :class="chosen_service===service.id ?  'bg-emerald-500 text-slate-100' : 'bg-slate-200'"
                      v-for="service in services" :key="service.id"
                      @click="ChooseService(service.id)">
                    <td class="block p-4 lg:px-6"> {{service.name}} </td>
                    <td class="p-4 lg:px-6"> {{service.department}} </td>
                    <td class="p-4 lg:px-6"> {{service.duration}} </td>
                    <td class="p-4 lg:px-6"> {{service.price}} </td>
                  </tr>
                </tbody>
              </table>
              </div>
              <div v-show="!services.length" class="rounded-b mb-0 px-4 py-3 border-0">
                <div class="flex flex-wrap items-center">
                  <div class="relative w-full px-4 max-w-full flex-grow flex-1">
                    <h3 class="font-semibold text-lg text-slate-800">
                      Empty
                    </h3>
                  </div>
                </div>
              </div>

            <div v-show="pages > 1" class="flex flex-nowrap px-4">
            <button class="flex-auto relative rounded transparent hover:shadow-lg py-3 w-3/12 fas fa-caret-left  fa-xl" @click="DecrementPage"></button>
            <div class="flex-none inline-block w-min-content">
              <button class="px-1 far fa-circle" :class="page == p ? 'fas' : ''" @click="UpdatePage(p)" v-for="(_, p) in pages" :key="p">
              </button>
            </div>
            <button class="flex-auto relative rounded transparent hover:shadow-lg py-3 w-3/12 fas fa-caret-right fa-xl" @click="IncrementPage"></button>
            </div>

            <div v-if="chosen_service" class="w-full inline-block relative mb-3">
              <div class="flex-wrap block uppercase text-slate-600 text-xs font-bold mb-2">
                Time <div class="inline-block text-rose-700 fa-2xs fa-solid fa-circle"></div>
              </div>
              <div>
                <div class="flex flex-nowrap">
                <button class="flex-auto relative rounded transparent hover:shadow-lg py-3 w-3/12 fas fa-caret-left  fa-xl" @click="PrevWeek"></button>
                <div class="flex-none inline-block w-min-content">
                  <div class="px-2">
                    {{week_schedules[weekat].month}} {{week_schedules[weekat].year}}
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
                      <td class="text-center align-middle" v-for="(week, didx) in week_schedules[weekat].days" :key="didx" >
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
                      v-for="(time,tidx) in week_schedules[weekat].days[dateat].times" :key="tidx" @click="ChooseTime(time, tidx)">{{time}}</button>
              <div v-if="week_schedules[weekat].days[dateat].times.length == 0">No time</div>
            </div>
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
                Request A Service
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

const today = new Date()

export default {
  data() {
    return {
      department:'',

      patient_iin: localStorage.getItem('user_iin'),
      services:  [],
      chosen_service:   '',
      week_schedules: [
        { month: 'October',
          year: '2022',
          days: [
            { date: '28', times: ['00:00', '00:15'], },
            { date: '29', times: ['00:00', '00:15'], },
            { date: '30', times: ['00:00', '00:30', '00:45'], },
            { date: '1', times: ['00:00', '00:15'], },
            { date: '2', times: ['00:00', '00:15', '00:30'], },
            { date: '3', times: ['00:00', '00:15'], },
            { date: '4', times: ['00:00', '00:30'], },
          ],
        },
        { month: 'November',
          year: '2022',
          days: [
              { date: '5', times: ['00:00', '00:15'], },
              { date: '6', times: ['00:00', '00:15'], },
              { date: '7', times: ['00:00', '00:30', '00:45'], },
              { date: '9', times: ['00:00', '00:15'], },
              { date: '10', times: ['00:00', '00:15', '00:30'], },
              { date: '11', times: ['00:00', '00:15'], },
              { date: '12', times: ['00:00', '00:30'], },
          ],
        },
      ],
      weekdays:['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],

      weekat: 0,
      dateat: 0,
      timeat:  undefined,
      timeidx: undefined,


      limit:  4,
      pages : 0,
      page  : 0,
      };
    },
    components: {
      //ToggleButton,
      RadioForm,
    // DoctorCard,
      //DatePick,
    },
    methods: {
      ChooseTime(time, tidx) {
        this.timeat  = time
        this.timeidx = tidx
      },
      ChooseService(sid) {
        this.chosen_service = sid
        this.weekat=0
        console.log(today.getDay())
        this.dateat=(today.getDay() || 7)-1
        this.timeat=undefined
        axios
          .get(`${server_url}/api/service/schedule/${this.chosen_service}/`, { headers: {"Authorization": 'Token ' + localStorage.access_token} })
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
        this.UpdateServices()
      },
      IncrementPage() {
        this.page += 1
        if (this.page >= this.pages) {
          this.page -=1
        }
        this.UpdateServices()
      },
      DecrementPage() {
        this.page -= 1
        if (this.page < 0) {
          this.page = 0
        }
        this.UpdateServices()
      },
      UpdateDepartment() {
        this.page = 0
        this.UpdateServices()
      },
      UpdateServices() {
        this.chosen_service = ''
        if (!this.department) {
          this.services = []
        }
        axios
          .get(`${server_url}/api/service/${this.department}/${this.limit}/${this.limit*this.page}/`, { headers: {"Authorization": 'Token ' + localStorage.access_token} })
          .then((response) => {
            console.log(response.data)
            this.services = response.data.services
            this.pages        = Math.ceil(response.data.count/this.limit)
          })
          .catch(function (error) {
            alert("Could not load Service")
            console.log(error)
          })
      },
      SendAppointment() {
        if (this.chosen_service && this.weekat>=0 && this.dateat >=0 && this.timeat) {
          console.log("token: " + localStorage.access_token)
          axios
            .post(`${server_url}/api/service/request/${this.patient_iin}/${this.chosen_service}/${this.weekat}/${this.dateat}/${this.timeat}/`, { headers: {"Authorization": 'Token ' + localStorage.access_token} })
            .then((response) => {
              console.log(response.data)
              this.week_schedules[this.weekat].days[this.dateat].times.splice(this.timeidx, 1)
              this.chosen_service = ''
              this.weekat=0
              this.dateat=(today.getDay() || 7)-1
              this.timeat=undefined
              alert("Success")
            })
            .catch(function (error) {
              alert("Could not make appointment")
              console.log(error)
            })
        }
      },
    }
};
</script>

