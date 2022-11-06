<template>
  <div
    class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded bg-white">
    <div class="rounded-t mb-0 px-4 py-3 border-0">
      <div class="flex flex-wrap items-center">
        <div class="relative w-full px-4 max-w-full flex-grow flex-1">
          <h3 class="font-semibold text-lg text-slate-700">
          Patients
          </h3>
        </div>
      </div>
    </div>
    <div class="block w-full overflow-x-auto">
      <!-- Projects table -->
      <table class="items-center w-full bg-transparent border-collapse">
        <thead>
          <tr>
            <th class="px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-center bg-blueGray-50 text-blueGray-500 border-blueGray-100">
              Name
            </th>
            <th class="px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-center bg-blueGray-50 text-blueGray-500 border-blueGray-100">
              Date of Birth
            </th>
            <th class="px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-center bg-blueGray-50 text-blueGray-500 border-blueGray-100">
              IIN
            </th>
            <th class="px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-center bg-blueGray-50 text-blueGray-500 border-blueGray-100">
              Contact Number
            </th>
            <th class="px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-center bg-blueGray-50 text-blueGray-500 border-blueGray-100">
              Address
            </th>
            <th class="px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-center bg-blueGray-50 text-blueGray-500 border-blueGray-100"></th>
          </tr>
        </thead>
        <tbody>
          <tr class="
            text-xs text-center align-middle whitespace-nowrap
            hover:text-white hover:bg-emerald-600
            focus:bg-emerald-600 focus:text-white focus:outline-none focus:ring-0
            active:bg-emerald-700 transition duration-150 ease-in-out
            border-t-1 border border-solid border-slate-200 border-l-0 border-r-0"
              v-for="(patient, pidx) in patients" :key="pidx"
              @click="$router.push({path: `/admin/patients/${patient.IIN}`})">
            <td class="block p-4 px-6"> {{patient.name}} {{patient.middlename}} {{patient.surname}} </td>
            <td class="p-4 px-6"> {{patient.date}} </td>
            <td class="p-4 px-6"> {{patient.IIN}} </td>
            <td class="p-4 px-6"> {{patient.contact_number}} </td>
            <td class="p-4 px-6"> {{patient.address}} </td>
            <td class="p-4 text-right"> <table-dropdown /> </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
<script>
import TableDropdown from "@/components/Dropdowns/TableDropdown.vue";


export default {

  data() {
    return {
      patients:[
        { name: 'Naruto',
          surname: 'Uzumaki',
          middlename: 'Hocage',
          date: '01.01.2001',
          IIN: '999999999999',
          contact_number: '87011112233',
          address: 'Konoha, Here street', },
        { name: 'Beka',
          surname: 'Me',
          middlename: 'Kab',
          date: '02.02.2002',
          IIN: '123456789321',
          contact_number: '87012223344',
          address: 'Astana, Street street', },
        { name: 'One',
          surname: 'Two',
          middlename: 'Three',
          date: '03.03.2003',
          IIN: '123456789000',
          contact_number: '87013334455',
          address: 'Astana, Not Here street', },
      ],
    };
  },
  components: {
    TableDropdown,
  },
};
</script>
