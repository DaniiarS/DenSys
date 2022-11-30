<template>
  <div class="container mx-auto flex content-center items-center justify-center h-full w-full">
    <div class="relative flex min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-slate-200 border-0">
      <div class="flex-auto px-4 lg:px-10 py-10 pt-0">
        <div class="text-slate-800 text-center py-3 font-bold">
          Doctor Appointment
        </div>
        <hr class="pb-4 border-t-1 border-slate-300" />
        <div class="flex-wrap">
          <div class="w-full px-4 inline-block relative mb-3">
            <div class="flex-wrap block uppercase text-slate-600 text-xs font-bold mb-2">
              Specialization <div class="inline-block text-rose-700 fa-2xs fa-solid fa-circle"></div>
            </div>
            <radio-form :buttons="['General','Pediatrist', 'Surgeon', 'Oculist', 'Neurologist']" v-model:input_type="specialization" @click="UpdateDoctors"/>
          </div>
          <div class="w-full px-4 inline-block relative">
            <div class="flex-wrap block uppercase text-slate-600 text-xs font-bold mb-2">
              Doctor <div class="inline-block text-rose-700 fa-2xs fa-solid fa-circle"></div>
            </div>
          </div>
          <div class="flex flex-wrap item-center">
            <doctor-card v-for="doctor in doctors_iins" :key="doctor.iin" :doctor_iin="doctor.iin"
              @click="ChooseDoctor(doctor.iin)" :isActive="doctor.iin == chosen_iin"/>
          </div>

          <div class="px-4">
          <button class="relative rounded transparent hover:shadow-lg py-3 w-6/12 fas fa-caret-left  fa-xl" @click="DecrementPage"></button>
          <button class="relative rounded transparent hover:shadow-lg py-3 w-6/12 fas fa-caret-right fa-xl" @click="IncrementPage"></button>
          </div>


          <div class="w-full px-4 inline-block relative mb-3">
            <div class="flex-wrap block uppercase text-slate-600 text-xs font-bold mb-2">
              Time <div class="inline-block text-rose-700 fa-2xs fa-solid fa-circle"></div>
            </div>
            <radio-form :buttons="['General','Pediatrist', 'Surgeon', 'Oculist', 'Neurologist']" v-model:input_type="specialization"/>
          </div>

          <div class="text-center px-4 mt-6" >
            <button class="bg-slate-800 text-white
                               active:bg-slate-600
                               text-sm font-bold uppercase
                               px-6 py-3 rounded mr-1 mb-1 w-full
                               shadow hover:shadow-lg
                               outline-none focus:outline-none
                               ease-linear transition-all duration-150"
                    @click="checkForm"
                    type="button">
              Make An Appointment
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import axios from 'axios'
import {server_url} from '@/api.js'

import RadioForm  from "@/components/RadioForm.vue"
import DoctorCard from '@/components/DoctorCard.vue';


export default {
  data() {
    return {
      specialization:'',
      doctors_iins:  [],
      chosen_iin:   '',
      limit: 4,
      offset:   0,
      count: 0,
    };
  },
  components: {
    //ToggleButton,
    RadioForm,
    DoctorCard,
    //DatePick,
  },
  methods: {
    ChooseDoctor(iin) {
      this.chosen_iin = iin
    },
    IncrementPage() {
      this.offset = (this.offset+this.limit)
      if (this.offset > this.count) {
        this.offset = this.offset-this.limit
      }
      this.UpdateDoctors()
    },
    DecrementPage() {
      this.offset = (this.offset-this.limit)
      if (this.offset < 0) {
        this.offset = 0
      }
      this.UpdateDoctors()
    },
    UpdateDoctors() {
      this.chosen_iin = ''
      if (!this.specialization) {
        this.doctors_iins = []
      }
      console.log(this.offset)
      console.log(this.limit)
      axios
        .get(`${server_url}/api/doctors/${this.specialization}/${this.limit}/${this.offset}/`, { headers: {"Authorization": 'Token ' + localStorage.access_token} })
        .then((response) => {
          console.log(response.data)
          this.doctors_iins = response.data.doctors
          this.count        = response.data.count
        })
        .catch(function (error) {
          alert("Could not load Doctor")
          console.log(error)
        })
    },
  }
};
</script>
