<template>
  <div class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded bg-slate-200">
    <div class="rounded-t mb-0 px-4 py-3 border-0">
      <div class="flex flex-wrap items-center">
        <div class="relative w-full px-4 max-w-full flex-grow flex-1">
          <h3 class="font-semibold text-lg text-slate-800">
            Patients
          </h3>
        </div>
      </div>
    </div>
    <div class="block w-full overflow-x-auto">
      <table class="items-center w-full border-collapse">
        <thead>
          <tr class="align-middle border border-solid text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-center text-slate-200 bg-slate-800 border-blueGray-100">
            <th class="px-6 py-3"> Name </th>
            <th class="px-6 py-3"> IIN </th>
            <th class="px-6 py-3"> Contact Number </th>
            <th class="px-6 py-3"> Total Apointments</th>
          </tr>
        </thead>
        <tbody>
          <tr class="text-xs text-center align-middle whitespace-nowrap
                     hover:text-slate-200 hover:bg-slate-800
                     focus:bg-slate-700 focus:text-slate-200 focus:outline-none focus:ring-0
                     active:bg-slate-600 transition duration-150 ease-in-out
                     border-t-1 border-solid border-slate-200 border-l-0 border-r-0"
              v-for="p in patients" :key="p.patient.iin"
              @click="$router.push({path: `/doctor/my-patients/${p.patient.iin}`})">
            <td class="p-4 px-6"> {{p.patient.name}} {{p.patient.surname}} </td>
            <td class="p-4 px-6"> {{p.patient.iin}} </td>
            <td class="p-4 px-6"> {{p.patient.contact_number}} </td>
            <td class="p-4 px-6"> {{p.pcount}} </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div v-show="!patients.length" class="rounded-b mb-0 px-4 py-3 border-0">
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
      patients:[
      ],
      status_map:['Requested', 'Scheduled', 'Completed', 'Overdue', 'Canceled'],
    };
  },
  components: {
  },
  methods: {
  },
  mounted () {
    if (localStorage.access_token) {
      console.log({Authorization: 'Token ' + localStorage.access_token})
      axios
        .get(server_url+'/api/doctor/patients/', { headers: {"Authorization": 'Token ' + localStorage.access_token} } )
        .then((response) => {
          console.log(response.data)
          this.patients          = response.data
          console.log(this.patients)
        })
        .catch(function (error) {
          alert("Could not load patients")
          console.log(error)
        })
    }
  }
};
</script>
