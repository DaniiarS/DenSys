<template>
  <div class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded bg-slate-200">
    <div class="rounded-t mb-0 px-4 py-3 border-0">
      <div class="flex flex-wrap items-center">
        <div class="relative w-full px-4 max-w-full flex-grow flex-1">
          <h3 class="font-semibold text-lg text-slate-800">
          Doctors
          </h3>
        </div>
      </div>
    </div>
    <div class="block w-full overflow-x-auto">
      <!-- Projects table -->
      <table class="items-center w-full border-collapse">
        <thead>
          <tr class="align-middle border border-solid text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-center text-slate-200 bg-slate-800 border-slate-100">
            <th class="px-6 py-3"> Name </th>
            <th class="px-6 py-3"> IIN </th>
            <th class="px-6 py-3"> Contact Number </th>
            <th class="px-6 py-3"> Departament </th>
            <th class="px-6 py-3"> Specialization </th>
            <th class="px-6 py-3"></th>
          </tr>
        </thead>
        <tbody @mouseout="activePhoto=null" id="button" aria-describedby="tooltip">
          <tr
            class="my-table-row
            text-xs text-center align-middle whitespace-nowrap
            group hover:text-slate-200 hover:bg-slate-800
            focus:bg-slate-700 focus:text-slate-200 focus:outline-none focus:ring-0
            active:bg-slate-600 transition duration-150 ease-in-out
            border-t-1 border border-solid border-slate-200 border-l-0 border-r-0"
              v-for="(doctor, didx) in doctors" :key="didx" :id="'r'+didx"
              @mouseover="updatePhoto(didx)"
              @click="$router.push({path: `/admin/doctors/${doctor.iin}`})">
            <td class="block p-4 px-6"> {{doctor.name}} {{doctor.middlename}} {{doctor.surname}} </td>
            <td class="p-4 px-6"> {{doctor.iin}} </td>
            <td class="p-4 px-6"> {{doctor.contact_number}} </td>
            <td class="p-4 px-6"> {{doctor.department}} </td>
            <td class="p-4 px-6"> {{doctor.specialization}} </td>
            <td class="p-4 text-right"> <table-dropdown /> </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div v-show="!doctors.length" class="rounded-b mb-0 px-4 py-3 border-0">
      <div class="flex flex-wrap items-center">
        <div class="relative w-full px-4 max-w-full flex-grow flex-1">
          <h3 class="font-semibold text-lg text-slate-800">
          Empty
          </h3>
        </div>
      </div>
    </div>
  </div>
  <img v-show="activePhoto" class="absolute w-24 h-32 top-1 left-1" :src="activePhoto"/>

  <div id="tooltip" role="tooltip">
    <div id="arrow" data-popper-arrow></div>
  </div>
</template>
<script>

import axios from 'axios'
import {server_url} from '@/api.js'

import TableDropdown from "@/components/TableDropdown.vue";

export default {

  data() {
    return {
      doctors:[],
      activePhoto: null,
    };
  },
  components: {
    TableDropdown,
  },
  methods: {
    updatePhoto(didx) {
      this.activePhoto = server_url+this.doctors[didx].photo
    }
  },
  mounted () {
    if (localStorage.access_token) {
      console.log({Authorization: 'Token ' + localStorage.access_token})
      axios
        .get( server_url+'/api'+'/doctors/', { headers: {"Authorization": 'Token ' + localStorage.access_token} } )
        .then((response) => {
          this.doctors = response.data
          //console.log(response)
        })
        .catch(function (error) {
          alert("Fail")
          console.log(error)
        })
    }
  }
};
</script>
