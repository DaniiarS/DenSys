<template>
  <div class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded bg-slate-200">
    <div class="rounded-t mb-0 px-4 py-3 border-0">
      <div class="flex flex-wrap items-center">
        <div class="relative w-full px-4 max-w-full flex-grow flex-1">
          <h3 class="font-semibold text-lg text-slate-800">
          Appointments
          </h3>
        </div>
      </div>
    </div>
    <div class="block w-full overflow-x-auto">
      <!-- Projects table -->
      <table class="items-center w-full border-collapse">
        <thead>
          <tr class="align-middle border border-solid text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-center text-slate-200 bg-slate-800 border-blueGray-100">
            <th class="px-6 py-3">
              Doctor
            </th>
            <th class="px-6 py-3">
              Date
            </th>
            <th class="px-6 py-3">
              Time
            </th>
            <th class="px-6 py-3">
              Status
            </th>
            <th class="px-6 py-3"></th>
          </tr>
        </thead>
        <tbody>
          <tr class="
            text-xs text-center align-middle whitespace-nowrap
            hover:text-slate-200 hover:bg-slate-800
            focus:bg-slate-700 focus:text-slate-200 focus:outline-none focus:ring-0
            active:bg-slate-600 transition duration-150 ease-in-out
            border-t-1 border-solid border-slate-200 border-l-0 border-r-0"
              v-for="(appointment, pidx) in appointments" :key="pidx"
              @click="$router.push({path: `/patient/appointments/${appointment.id}`})">
            <td class="block p-4 px-6"> {{appointment.doctor.name}} {{appointment.doctor.surname}} </td>
            <td class="p-4 px-6"> {{appointment.date}} </td>
            <td class="p-4 px-6"> {{appointment.time}} </td>
            <td class="p-4 px-6"> {{appointment.is_active}} </td>
            <td class="p-4 text-right"> <table-dropdown /> </td>
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

import axios from 'axios'
import {server_url} from '@/api.js'

import TableDropdown from "@/components/TableDropdown.vue";

export default {

  data() {
    return {
      appointments:[
      ],
      doctors:{}
    };
  },
  components: {
    TableDropdown,
  },
  mounted () {
    if (localStorage.access_token) {
      console.log({Authorization: 'Token ' + localStorage.access_token})
      axios
        .get(server_url+'/api/appointments/', { headers: {"Authorization": 'Token ' + localStorage.access_token} } )
        .then((response) => {
          console.log(response.data)
          this.appointments = response.data
        })
        .catch(function (error) {
          alert("Could not load appointments")
          console.log(error)
        })
    }
  }
};
</script>
