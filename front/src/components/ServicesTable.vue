<template>
    <div class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded bg-slate-200">
      <div class="rounded-t mb-0 px-4 py-3 border-0">
        <div class="flex flex-wrap items-center">
          <div class="relative w-full px-4 max-w-full flex-grow flex-1">
            <h3 class="font-semibold text-lg text-slate-800">
            Services
            <search-table :input="all_services" v-model:output="services"/>
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
              <th class="px-6 py-3"> Department </th>
              <th class="px-6 py-3"> Service Duration </th>
              <th class="px-6 py-3"> Service Price </th>
            </tr>
          </thead>
          <tbody>
            <tr class="
              text-xs text-center align-middle whitespace-nowrap
              hover:bg-slate-300
              active:bg-slate-400 transition duration-150 ease-in-out
              border-t-1 border-solid border-slate-200 border-l-0 border-r-0"
                v-for="(service, pidx) in services" :key="pidx"
                @click="$router.push({path: `/admin/services/${service.id}`})">
              <td class="block p-4 px-6"> {{service.name}} </td>
              <td class="p-4 px-6"> {{service.department}} </td>
              <td class="p-4 px-6"> {{service.duration}} </td>
              <td class="p-4 px-6"> {{service.price}} </td>
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

  import axios        from 'axios'
  import {server_url} from '@/api.js'

  import SearchTable  from "@/components/SearchTable.vue";

  export default {

    data() {
      return {
        services:[],
        all_services:[],
      };
    },
    components: {
      SearchTable,
    },
    mounted () {
      if (localStorage.access_token) {
        console.log({Authorization: 'Token ' + localStorage.access_token})
        axios
          .get(server_url+'/api/services', { headers: {"Authorization": 'Token ' + localStorage.access_token} } )
          .then((response) => {
            console.log(response.data)
            this.services     = response.data
            this.all_services = this.services
          })
          .catch(function (error) {
            alert("Could not load service")
            console.log(error)
          })
      }
    }
  };
  </script>

