<template>
  <div class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded bg-slate-200">
    <div class="rounded-t mb-0 px-4 py-3 border-0">
      <div class="flex flex-wrap items-center">
        <div class="relative w-full px-4 max-w-full flex-grow flex-1">
          <h3 class="font-semibold text-lg text-slate-800">
            Requests
            <search-table :input="all_sorted_schedules" v-model:output="sorted_schedules"/>
          </h3>
        </div>
      </div>
    </div>
    <div class="block w-full overflow-x-auto">
      <!-- Projects table -->
      <table class="items-center w-full border-collapse">
        <thead>
          <tr class="align-middle border border-solid text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-center text-slate-200 bg-slate-800 border-blueGray-100">
            <th class="px-6 py-3"> </th>
            <th class="px-6 py-3"> Patient </th>
            <th class="px-6 py-3"> IIN </th>
            <th class="px-6 py-3"> Date </th>
            <th class="px-6 py-3"> Time </th>
          </tr>
        </thead>
        <tbody>
          <tr class="
            text-xs text-center align-middle whitespace-nowrap
            hover:bg-slate-300
            active:bg-slate-400 transition duration-150 ease-in-out
            border-t-1 border-solid border-slate-200 border-l-0 border-r-0"
              v-for="(schedule, sidx) in sorted_schedules" :key="sidx"
              @click="PickedSchedule(schedule)">
            <td class="block p-4 px-6">
              <div v-if="schedule.doctor" class="flex-wrap block uppercase text-slate-500 text-xs mb-2">
                Appointment:
                <a class="text-slate-600 font-bold normal-case">
                  Doctor {{schedule.doctor.name}} {{schedule.doctor.surname}}
                </a>
              </div>
              <div v-if="!schedule.doctor" class="flex-wrap block uppercase text-slate-500 text-xs mb-2">
                Service:
                <a class="text-slate-600 font-bold normal-case">
                  {{schedule.service.name}}
                </a>
              </div>
            </td>
            <td class="p-4 px-6">
              {{schedule.patient.name}} {{schedule.patient.surname}}
            </td>
            <td class="p-4 px-6">
              {{schedule.patient.iin}}
            </td>
            <td class="p-4 px-6">
              {{schedule.date}}
            </td>
            <td class="p-4 px-6"> {{schedule.time}} </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div v-show="!sorted_schedules.length" class="rounded-b mb-0 px-4 py-3 border-0">
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

import axios        from 'axios'
import {server_url} from '@/api.js'
import SearchTable  from "@/components/SearchTable.vue";

export default {

  data() {
    return {
      appointments:[],
      service_requests:[],
      sorted_schedules:[],
      all_sorted_schedules:[],
      status_map:['Requested', 'Approved', 'Overdue', 'Completed', 'Canceled'],
      month:['January', 'Feburary', 'March', 'April', 'May','June','July', 'August', 'September', 'October', 'November', 'December'],
    };
  },
  components: {
    SearchTable
  },
  methods: {
    formatDates(as) {
      for (const a of as) {
        let d = new Date(a.date)
        a.date = this.month[d.getMonth()] + ' ' + d.getDate() + ', ' + d.getFullYear()
      }
    },
    formatStatuses(as) {
      for (const a of as) {
        a.status = this.status_map[a.status]
      }
    },
    PickedSchedule(schedule) {
      if (schedule.doctor) {
        this.$router.push({path: `/admin/appointment/${schedule.id}`})
      } else {
        this.$router.push({path: `/admin/service-request/${schedule.id}`})
      }
    },
    sort_schedules() {
      var result = []
      const as = this.appointments
      const ss = this.service_requests
      var a = 0
      var s = 0
      while (a < as.length && s < ss.length) {
        if (as[a].date < ss[s].date || (as[a].date == ss[s].date && as[a].time < ss[s].time)) {
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
      return result
    }
  },
  mounted () {
    const iin = localStorage.user_iin
    console.log(iin)
    if (localStorage.access_token) {
      console.log({Authorization: 'Token ' + localStorage.access_token})
      axios
        .get(server_url+'/api/patient/requests/'+iin, { headers: {"Authorization": 'Token ' + localStorage.access_token} } )
        .then((response) => {
          console.log(response.data)
          this.appointments     = response.data.appointments
          this.service_requests = response.data.service_requests
          this.sorted_schedules = this.sort_schedules()
          this.formatDates(this.sorted_schedules)
          this.formatStatuses(this.sorted_schedules)
          this.all_sorted_schedules = this.sorted_schedules
          console.log(this.sorted_schedules)
        })
        .catch(function (error) {
          alert("Could not load appointments")
          console.log(error)
        })
    }
  }
};
</script>
