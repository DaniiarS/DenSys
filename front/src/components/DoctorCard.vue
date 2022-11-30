<template>
  <div class="flex-auto mb-8 px-4 lg:max-w-6/12 break-words">
    <div class="relative flex px-4 py-3 bg-slate-100 rounded items-center
                shadow-lg cursor-pointer hover:shadow-none
                ease-linear transition-all duration-150 ">
      <div v-if="isActive" class="absolute right-2.5 fa-xl fas fa-check text-emerald-500"></div>
      <div class="w-24 lg:w-32">
        <img :src="photo"/>
      </div>
      <div class="">
        <div class="px-4 relative w-full mb-3">
          <div class="block text-slate-800 text-xl font-bold">
            Dr. {{doctor.name}} {{doctor.surname}}
          </div>
          <div class="block text-slate-400 mb-2">
            {{doctor.specialization}}
            <a v-if="doctor.category != 'None'">
              {{doctor.category}} Category
            </a>
          </div>
          <div class="flex-wrap block uppercase text-slate-600 text-xs font-bold mb-2">
            <div class="fa-2xs fa-solid fa-phone"></div> {{doctor.contact_number}}
          </div>
          <div class="flex-wrap block uppercase text-slate-400 text-xs mb-2">
            Experience:
            <a class="text-slate-600 font-bold lowercase">
            {{doctor.experience}} years
            </a>
          </div>
          <div class="flex-wrap block uppercase text-slate-400 text-xs">
            Price:
            <a class="text-slate-600 font-bold lowercase">
            {{doctor.price}} tenge
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import {server_url} from '@/api.js'

import blankDoctor from "@/assets/img/blankDoctor.jpg";

export default {
  data() {
    return {
      doctor:{},
      photo: blankDoctor,
    };
  },
  props: {
    doctor_iin: {
      type: String,
      default: ''
    },
    isActive: {
      type: Boolean,
      default: false
    },
  },
  components: {
    //ToggleButton,
    //DatePick,
  },
  methods: {
  },
  mounted() {
    axios
      .get(`${server_url}/api/doctor/${this.doctor_iin}`, { headers: {"Authorization": 'Token ' + localStorage.access_token} })
      .then((response) => {
        this.doctor = response.data
        this.photo = server_url + this.doctor.photo
      })
      .catch(function (error) {
        alert("Could not load Doctor")
        console.log(error)
      })
  }
};
</script>
