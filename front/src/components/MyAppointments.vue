<template>
  <div class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded bg-slate-200">
    <div class="rounded-t mb-0 px-4 py-3 border-0">
      <div class="flex flex-wrap items-center">
        <div class="relative w-full px-4 max-w-full flex-grow flex-1">
          <h3 class="font-semibold text-lg text-slate-800">
            Appointments
            <search-table :input="all_appointments" v-model:output="appointments"/>
          </h3>
        </div>
      </div>
    </div>
    <div class="block w-full overflow-x-auto">
      <!-- Projects table -->
      <table class="items-center w-full border-collapse">
        <thead>
          <tr class="align-middle border border-solid text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-center text-slate-200 bg-slate-800 border-blueGray-100">
            <th class="px-6 py-3"> Name   </th>
            <th class="px-6 py-3"> IIN    </th>
            <th class="px-6 py-3"> Contact Number </th>
            <th class="px-6 py-3"> Date   </th>
            <th class="px-6 py-3"> Time   </th>
            <th class="px-6 py-3"> Status </th>
          </tr>
        </thead>
        <tbody>
          <tr class="text-xs text-center align-middle whitespace-nowrap
                     hover:bg-slate-300
                     active:bg-slate-400 transition duration-150 ease-in-out
                     border-t-1 border-solid border-slate-200 border-l-0 border-r-0"
              v-for="appointment in appointments" :key="appointment.id"
              @click="$router.push({path: `/doctor/my-appointments/${appointment.id}`})">
            <td class="block p-4 px-6">
              {{appointment.patient.name}} {{appointment.patient.surname}}
            </td>
            <td class="p-4 px-6"> {{appointment.patient.iin}} </td>
            <td class="p-4 px-6"> {{appointment.patient.contact_number}} </td>
            <td class="p-4 px-6">
              {{appointment.date}}
            </td>
            <td class="p-4 px-6"> {{appointment.time}} </td>
            <td class="p-4 px-6"> {{appointment.status}} </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div v-show="!appointments.length" class="rounded-b mb-0 px-4 py-3 border-0">
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
      all_appointments:[],
      status_map:['Requested', 'Approved', 'Overdue', 'Completed', 'Canceled'],
      month:['January', 'Feburary', 'March', 'April', 'May','June','July', 'August', 'September', 'October', 'November', 'December'],
    };
  },
  components: {
    SearchTable,
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
  },
  mounted () {
    if (localStorage.access_token) {
      console.log({Authorization: 'Token ' + localStorage.access_token})
      axios
        .get(server_url+'/api/doctor/appointments/', { headers: {"Authorization": 'Token ' + localStorage.access_token} } )
        .then((response) => {
          console.log(response.data)
          this.appointments = response.data
          this.formatDates(this.appointments)
          this.formatStatuses(this.appointments)
          this.all_appointments = this.appointments
        })
        .catch(function (error) {
          alert("Could not load appointments")
          console.log(error)
        })
    }
  }
};
</script>
