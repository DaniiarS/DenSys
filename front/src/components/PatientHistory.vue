<template>
  <div class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded bg-slate-200">
    <div class="rounded-t mb-0 px-4 py-3 border-0">
      <div class="flex flex-wrap items-center">
        <div class="relative w-full px-4 max-w-full flex-grow flex-1">
          <h3 class="font-semibold text-lg text-slate-800">
            Patient History <a v-if="patient && who !== 'patient'">{{patient.name}} {{patient.surname}} {{patient.iin}}</a>
          </h3>
        </div>
      </div>
    </div>
    <div v-if="history" class="block w-full overflow-x-auto">
      <!-- Projects table -->
      <table class="items-center w-full border-collapse">
        <thead>
          <tr class="align-middle border border-solid text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-center text-slate-200 bg-slate-800 border-blueGray-100">
            <th class="px-6 py-3"> </th>
            <th class="px-6 py-3"> Date </th>
            <th class="px-6 py-3"> Time </th>
            <th class="px-6 py-3"> Status </th>
          </tr>
        </thead>
        <tbody>
          <tr class="text-xs text-center align-middle whitespace-nowrap
                     border-t-1 border-solid border-slate-200 border-l-0 border-r-0"
              v-for="h in history" :key="h.id">
            <td class="p-4 px-6">
              <div v-if="h.aid" class="flex-wrap block uppercase text-slate-400 text-xs mb-2">
                Appointment:
                <a class="text-slate-600 font-bold normal-case">
                  Doctor {{h.aid.doctor.name}} {{h.aid.doctor.surname}}
                </a>
              </div>
              <div v-if="!h.aid" class="flex-wrap block uppercase text-slate-400 text-xs mb-2">
                Service:
                <a class="text-slate-600 font-bold normal-case">
                  {{h.srid.service.name}}
                </a>
              </div>
            </td>
            <td class="p-4 px-6">
              {{month[h.when_made.getMonth()]}} {{h.when_made.getDate()}}, {{h.when_made.getFullYear()}}
            </td>
            <td class="p-4 px-6">
              {{hours(h.when_made)}}:{{minutes(h.when_made)}}
            </td>
            <td class="p-4 px-6"> {{status_map[h.status]}} </td>
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
      iin:undefined,
      who:'',
      patient:{name:'', surname:'', iin:''},
      status_map:['Requested', 'Approved', 'Overdue', 'Completed', 'Canceled'],
      month:['January', 'Feburary', 'March', 'April', 'May','June','July', 'August', 'September', 'October', 'November', 'December'],
      history:[],
      appointments:[],
      services:[],
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
    formatHistory(history) {
      for (const h of history) {
        h.when_made = new Date(h.when_made)
      }
    },
    sort_history() {
      var result = []
      const as = this.appointments
      const ss = this.services
      var a = 0
      var s = 0
      while (a < as.length && s < ss.length) {
        if (as[a].when_made > ss[s].when_made) {
          result.push(as[a])
          a++
        } else {
          result.push(ss[s])
          s++
        }
      }
      while (a < as.length) {
        result.push(as[a])
        a++
      }
      while (s < ss.length) {
        result.push(ss[s])
        s++
      }
      this.formatHistory(result)
      return result
    }
  },
  mounted() {
    this.who = localStorage.who
    this.iin = localStorage.user_iin
    if (this.$route.params.iin) {
      this.iin = this.$route.params.iin
    }
    axios
      .get(`${server_url}/api/patient/history/${this.iin}`, { headers: {"Authorization": 'Token ' + localStorage.access_token} })
      .then((response) => {
        console.log(response.data)
        this.patient      = response.data.patient
        this.appointments = response.data.appointments
        this.services     = response.data.services
        this.history = this.sort_history()
        console.log(this.history)
      })
      .catch(function (error) {
        alert("Could not load Doctor")
        console.log(error)
      })
  }
};
</script>
