<template>
    <div class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded bg-slate-200">
      <div class="rounded-t mb-0 px-4 py-3 border-0">
        <div class="flex flex-wrap items-center">
          <div class="relative w-full px-4 max-w-full flex-grow flex-1">
            <h3 class="font-semibold text-lg text-slate-800">
            Services
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
                Department
              </th>
              <th class="px-6 py-3">
                Service Duration
              </th>
              <th class="px-6 py-3">
                Service Price
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
                v-for="(service, pidx) in services" :key="pidx"
                @click="$router.push({path: `/admin/service/${service.id}`})">
              <td class="block p-4 px-6"> {{service.name}} </td>
              <td class="p-4 px-6"> {{service.department}} </td>
              <td class="p-4 px-6"> {{service.duration}} </td>
              <td class="p-4 px-6"> {{service.price}} </td>
              <td class="p-4 text-right"> <table-dropdown /> </td>
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
    </div>
  </template>
  <script>
  
  import axios from 'axios'
  import {server_url} from '@/api.js'
  
  import TableDropdown from "@/components/TableDropdown.vue";
  
  export default {
  
    data() {
      return {
        services:[
        ],
      };
    },
    components: {
      TableDropdown,
    },
    mounted () {
      if (localStorage.access_token) {
        console.log({Authorization: 'Token ' + localStorage.access_token})
        axios
          .get(server_url+'/api/service', { headers: {"Authorization": 'Token ' + localStorage.access_token} } )
          .then((response) => {
            console.log(response.data)
            this.services = response.data
          })
          .catch(function (error) {
            alert("Could not load service")
            console.log(error)
          })
      }
    }
  };
  </script>
  