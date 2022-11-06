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
          <tr class="align-middle border border-solid text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-center text-slate-200 bg-slate-800 border-blueGray-100">
            <th class="px-6 py-3">
              Name
            </th>
            <th class="px-6 py-3">
              IIN
            </th>
            <th class="px-6 py-3">
              Contact Number
            </th>
            <th class="px-6 py-3">
              Departament
            </th>
            <th class="px-6 py-3">
              Specialization
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
            border-t-1 border border-solid border-slate-200 border-l-0 border-r-0"
              v-for="(doctor, didx) in doctors" :key="didx"
              @click="$router.push({path: `/admin/doctors/${doctor.iin}`})">
            <td class="block p-4 px-6"> {{doctor.name}} {{doctor.middlename}} {{doctor.surname}} </td>
            <td class="p-4 px-6"> {{doctor.iin}} </td>
            <td class="p-4 px-6"> {{doctor.contact_number}} </td>
            <td class="p-4 px-6"> {{doctor.departament}} </td>
            <td class="p-4 px-6"> {{doctor.specialization}} </td>
            <td class="p-4 text-right"> <table-dropdown /> </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
<script>
import axios from 'axios'

import TableDropdown from "@/components/TableDropdown.vue";

export default {

  data() {
    return {
      doctors:[
      ],
    };
  },
  components: {
    TableDropdown,
  },
  mounted () {
    console.log(this.$route.params.iin)
    axios
      .get('http://localhost:8000/api/doctors')
      .then((response) => {
        console.log(response.data)
        this.doctors = response.data
      })
      .catch(function (error) {
        alert("Fail")
        console.log(error)
      })
  }
};
</script>
