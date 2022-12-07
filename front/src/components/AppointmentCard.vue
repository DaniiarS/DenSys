<template>
  <div class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded bg-slate-200">
    <div class="rounded-t mb-0 px-4 py-3 border-0">
      <div class="flex flex-wrap items-center">
        <div class="relative w-full px-4 max-w-full flex-grow flex-1">
          <h3 class="font-semibold text-lg text-slate-800">
            Appointment with
            <a v-if="appointment && (who=='doctor' || who=='admin')">{{appointment.patient.name}} {{appointment.patient.surname}}</a>
            <a v-if="appointment && who=='admin'"> And </a>
            <a v-if="appointment && (who=='patient' || who=='admin')">Doctor {{appointment.doctor.name}} {{appointment.doctor.surname}}</a>
            <a v-if="appointment"> at {{appointment.time}} {{date(appointment.date)}}</a>
            <button v-if="(who=='admin') && appointment && appointment.status === 0"
                    class="mx-2 text-slate-100 px-4 shadow-lg bg-emerald-500 rounded hover:shadow active:bg-emerald-600"
                    @click="ChangeAppointmentStatus(1)"
                    >
              Approve
            </button>
            <button v-if="(who=='doctor') && appointment && appointment.status === 1"
                    class="mx-2 text-slate-100 px-4 shadow-lg bg-emerald-500 rounded hover:shadow active:bg-emerald-600"
                    @click="ChangeAppointmentStatus(3)"
                    >
              Complete
            </button>
            <button v-if="appointment && appointment.status !== 4 && appointment.status !== 3"
                    class="mx-2 text-slate-100 px-4 shadow-lg bg-rose-500 rounded hover:shadow active:bg-rose-600"
                    @click="ChangeAppointmentStatus(4)"
                    >
              Cancel
            </button>
          </h3>
        </div>
      </div>
    </div>
    <div v-if="history" class="block w-full overflow-x-auto">
      <!-- Projects table -->
      <table class="items-center w-full border-collapse">
        <thead>
          <tr class="align-middle border border-solid text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-center text-slate-200 bg-slate-800 border-blueGray-100">
            <th class="px-6 py-3"> Status </th>
            <th class="px-6 py-3"> Date </th>
            <th class="px-6 py-3"> Time </th>
          </tr>
        </thead>
        <tbody>
          <tr class="text-xs text-center align-middle whitespace-nowrap
                     border-t-1 border-solid border-slate-200 border-l-0 border-r-0"
              v-for="h in history" :key="h.id">
            <td class="p-4 px-6"> {{status_map[h.status]}} </td>
            <td class="p-4 px-6">
              {{month[h.when_made.getMonth()]}} {{h.when_made.getDate()}}, {{h.when_made.getFullYear()}}
            </td>
            <td class="p-4 px-6">
              {{hours(h.when_made)}}:{{minutes(h.when_made)}}
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div v-if="history && !history.length" class="rounded-b mb-0 px-4 py-3 border-0">
      <div class="flex flex-wrap items-center">
        <div class="relative w-full px-4 max-w-full flex-grow flex-1">
          <h3 class="font-semibold text-lg text-slate-800">
          Empty
          </h3>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import {server_url} from '@/api.js'

export default {
  data() {
    return {
      who: undefined,
      aid: undefined,
      status_map:['Requested', 'Approved', 'Overdue', 'Completed', 'Canceled'],
      month:['January', 'Feburary', 'March', 'April', 'May','June','July', 'August', 'September', 'October', 'November', 'December'],
      appointment:{patient:{name:'', surname:''}, doctor:{name:'', surname:''}, date: new Date(), time:'11:41'},
      history:null,
    };
  },
  props: {
  },
  components: {
    //ToggleButton,
    //DatePick,
  },
  methods: {
    hours(datetime) {
      var result = datetime.getHours() < 10 ? '0' : ''
      result += datetime.getHours()
      return result
    },
    minutes(datetime) {
      var result = datetime.getMinutes() < 10 ? '0' : ''
      result += datetime.getMinutes()
      return result
    },
    date(d) {
      var result = this.month[d.getMonth()] + ' ' + d.getDate() + ', ' + d.getFullYear()
      return result
    },
    formatDate(a) {
      a.date = new Date(a.date)
    },
    ChangeAppointmentStatus(status) {
      this.appointment.status = status // 3 - Complete, 4 - Cancel
      axios
        .put(`${server_url}/api/appointment/${this.aid}`, this.appointment, { headers: {"Authorization": 'Token ' + localStorage.access_token} })
        .then((response) => {
          console.log(response.data)
          this.appointment = response.data.appointment
          this.history     = response.data.history
          this.formatDate(this.appointment)
          this.formatHistory(this.history)
          console.log(this.history)

        })
        .catch(function (error) {
          alert("Could not load Doctor")
          console.log(error)
        })
    },
    CancelAppointment() {
      this.appointment.status = 4 // Cancel
      axios
        .put(`${server_url}/api/appointment/${this.aid}`, this.appointment, { headers: {"Authorization": 'Token ' + localStorage.access_token} })
        .then((response) => {
          console.log(response.data)
          this.appointment = response.data.appointment
          this.history     = response.data.history
          this.formatDate(this.appointment)
          this.formatHistory(this.history)
          console.log(this.history)

        })
        .catch(function (error) {
          alert("Could not load Doctor")
          console.log(error)
        })
    },
    formatHistory(history) {
      for (const h of history) {
        h.when_made = new Date(h.when_made)
      }
    }
  },
  mounted() {
    this.aid = this.$route.params.aid
    this.who = localStorage.who
    axios
      .get(`${server_url}/api/appointment/${this.aid}`, { headers: {"Authorization": 'Token ' + localStorage.access_token} })
      .then((response) => {
        console.log(response.data)
        this.appointment = response.data.appointment
        this.history     = response.data.history
        this.formatDate(this.appointment)
        this.formatHistory(this.history)
        console.log(this.history)

      })
      .catch(function (error) {
        alert("Could not load Doctor")
        console.log(error)
      })
  }
};
</script>
