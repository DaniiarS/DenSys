<template>
  <div class="container mx-auto h-full w-full lg:w-full flex content-center items-center justify-center h-full">
    <div class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-slate-200 border-0">
      <div class="flex-auto px-4 lg:px-10 py-10 pt-0">
        <div class="text-slate-800 text-center py-3 font-bold">
          Patient Information
        </div>
        <hr class="pb-4 border-t-1 border-slate-300" />
        <div class="flex-wrap">
          <div class="w-full lg:w-4/12 px-4 inline-block relative mb-3">
            <div class="flex-wrap block uppercase text-slate-600 text-xs font-bold mb-2">
              Name <div class="inline-block text-rose-700 fa-2xs fa-solid fa-circle"></div>
              <div class="inline-block px-4 text-rose-700"
                   v-if="errors.get('name') && !validName(patient.name)">
                {{errors.get('name')}}
              </div>
            </div>
            <input type="text"
                   v-model="patient.name"
                   class="w-full relative border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring ease-linear transition-all duration-150"
                   :class="[errors.size && !validName(patient.name) ? 'border-2 border-rose-700' : 'border-0' ]"
                   placeholder="Name"/>

          </div>
          <div class="w-full lg:w-4/12 px-4 inline-block relative mb-3">
            <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
              Surname <div class="text-rose-700 fa-2xs fa-solid fa-circle"></div>
              <div class="inline-block px-4 text-rose-700"
                   v-if="errors.get('surname') && !validName(patient.surname)">
                {{errors.get('surname')}}
              </div>
            </label>
            <input type="text"
                   v-model="patient.surname"
                   class="w-full relative border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring ease-linear transition-all duration-150"
                   :class="[errors.size && !validName(patient.surname) ? 'border-2 border-rose-700' : 'border-0' ]"
                   placeholder="Surname"/>
          </div>
          <div class="w-full lg:w-4/12 px-4 inline-block relative mb-3">
            <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
              Middlename <div class="text-rose-700 fa-2xs fa-solid fa-circle"></div>
              <div class="inline-block px-4 text-rose-700"
                   v-if="errors.get('middlename') && !validName(patient.middlename)">
                {{errors.get('middlename')}}
              </div>
            </label>
            <input type="text"
                   v-model="patient.middlename"
                   class="w-full relative border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring ease-linear transition-all duration-150"
                   :class="[errors.size && !validName(patient.middlename) ? 'border-2 border-rose-700' : 'border-0' ]"
                   placeholder="Middlename"/>
          </div>
          <div class="w-full lg:w-4/12 px-4 inline-block relative mb-3">
            <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
              Date of Birth<div class="text-slate-600 fa-2xs fa-solid fa-circle"></div>
              <div class="inline-block px-4 text-rose-700"
                   v-if="errors.get('date') && !validDate(patient.date)">
                {{errors.get('date')}}
              </div>
            </label>
            <date-pick v-model:value="patient.date"
                       :isDisabled="true"
                       :selectableYearRange="{from: 1930, to: 2022}"
                       :format="'DD.MM.YYYY'"/>
          </div>
          <div class="w-full lg:w-4/12 px-4 inline-block relative mb-3">
            <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
              IIN number <div class="text-slate-600 fa-2xs fa-solid fa-circle"></div>
              <div class="inline-block px-4 text-rose-700"
                   v-if="errors.get('iin') && !validID(patient.iin)">
                {{errors.get('iin')}}
              </div>
            </label>
            <input type="text"
                   v-model="patient.iin"
                   disabled
                   class="border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150 disabled:text-slate-300"
                   :class="[errors.size && !validID(patient.iin) ? 'border-2 border-rose-700' : 'border-0' ]"
                   placeholder="IIN number"/>
          </div>
          <div class="w-full lg:w-4/12 px-4 inline-block relative mb-3">
            <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
              ID number <div class="text-rose-700 fa-2xs fa-solid fa-circle"></div>
              <div class="inline-block px-4 text-rose-700"
                   v-if="errors.get('id') && !validID(patient.id)">
                {{errors.get('id')}}
              </div>
            </label>
            <input type="text"
                   v-model="patient.id"
                   class="border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                   :class="[errors.size && !validID(patient.id) ? 'border-2 border-rose-700' : 'border-0' ]"
                   oninput="this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*)\./g, '$1');"
                   placeholder="id number"/>
          </div>
          <div class="px-4 relative w-full mb-3">
            <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
              Blood Type <div class="text-rose-700 fa-2xs fa-solid fa-circle"></div>
              <div class="inline-block px-4 text-rose-700"
                   v-if="errors.get('blood_type') && !(patient.blood_type)">
                {{errors.get('blood_type')}}
              </div>
            </label>
            <radio-form :class="[errors.size && !patient.blood_type ? 'border-2 border-rose-700' : 'border-0' ]" :buttons="['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']" v-model:input_type="patient.blood_type"/>
          </div>
          <div class="px-4 relative w-full mb-3">
            <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
              Marital Status <div class="text-rose-700 fa-2xs fa-solid fa-circle"></div>
              <div class="inline-block px-4 text-rose-700"
                   v-if="errors.get('marital_status') && !(patient.marital_status)">
                {{errors.get('marital_status')}}
              </div>
            </label>
            <radio-form :class="[errors.size && !patient.marital_status ? 'border-2 border-rose-700' : 'border-0' ]" :buttons="['Married', 'Single', 'Divorced', 'Widowed']" v-model:input_type="patient.marital_status"/>
          </div>

          <div class="w-full lg:w-6/12 px-4 inline-block relative mb-3">
            <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
              Contact Number <div class="text-rose-700 fa-2xs fa-solid fa-circle"></div>
              <div class="inline-block px-4 text-rose-700"
                   v-if="errors.get('contact_number') && !(patient.contact_number)">
                {{errors.get('contact_number')}}
              </div>
            </label>
            <input type="text"
                   v-model="patient.contact_number"
                   class="border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                   :class="[errors.size && !(patient.contact_number) ? 'border-2 border-rose-700' : 'border-0' ]"
                   placeholder="Contact Number"
                   oninput="this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*)\./g, '$1');" />
          </div>
          <div class="w-full lg:w-6/12 px-4 inline-block relative mb-3">
            <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
              Emergency Contact Number <div class="text-rose-700 fa-2xs fa-solid fa-circle"></div>
              <div class="inline-block px-4 text-rose-700"
                   v-if="errors.get('emergency_contact_number') && !(patient.emergency_contact_number)">
                {{errors.get('emergency_contact_number')}}
              </div>
            </label>
            <input type="text"
                   v-model="patient.emergency_contact_number"
                   class="border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                   :class="[errors.size && !(patient.emergency_contact_number) ? 'border-2 border-rose-700' : 'border-0' ]"
                   oninput="this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*)\./g, '$1');"
                   placeholder="Emergency Contact Number"/>
          </div>
          <div class="w-full lg:w-6/12 px-4 inline-block relative mb-3">
            <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
              Email (Optional)
            </label>
            <input type="email"
                   v-model="patient.email"
                   class="border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                   placeholder="Email"/>
          </div>
          <div class="w-full lg:w-6/12 px-4 inline-block relative mb-3">
            <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
              Address <div class="text-rose-700 fa-2xs fa-solid fa-circle"></div>
              <div class="inline-block px-4 text-rose-700"
                   v-if="errors.get('address') && !(patient.address)">
                {{errors.get('address')}}
              </div>
            </label>
            <input type="text"
                   v-model="patient.address"
                   :class="[errors.size && !patient.address ? 'border-2 border-rose-700' : 'border-0' ]"
                   class="border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                   placeholder="Address"/>
          </div>
          <div class="w-full lg:w-6/12 px-4 inline-block relative mb-3">
            <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
              Password <div class="text-rose-700 fa-2xs fa-solid fa-circle"></div>
              <div class="inline-block px-4 text-rose-700"
                   v-if="errors.get('password') && (!patient.password || patient.password !== repeat_password)">
                {{errors.get('password')}}
              </div>
            </label>
            <input type="text"
                   v-model="patient.password"
                   :class="[errors.size && !patient.password ? 'border-2 border-rose-700' : 'border-0' ]"
                   class="border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                   placeholder="Password"/>
          </div>
          <div class="w-full lg:w-6/12 px-4 inline-block relative mb-3">
            <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
              Repeat Password <div class="text-rose-700 fa-2xs fa-solid fa-circle"></div>
              <div class="inline-block px-4 text-rose-700"
                   v-if="errors.get('repeat') && patient.password !== repeat_password">
                {{errors.get('repeat')}}
              </div>
            </label>
            <input type="text"
                   v-model="patient.password"
                   :class="[errors.size && !patient.password ? 'border-2 border-rose-700' : 'border-0' ]"
                   class="border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                   placeholder="Password"/>
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
              Update Patient Information
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

import RadioForm from "@/components/RadioForm.vue"
import DatePick from '@/components/vueDatePick.vue';


export default {
  name: "patient-register",
  data() {
    return {
      test: '',
      errors: new Map(),
      patient: {
        name: '',
        surname: '',
        middlename: '',
        date: '',
        iin: '',
        id: '',
        blood_type: '',
        marital_status: '',
        contact_number: '',
        emergency_contact_number: '',
        email: '',
        address: '',
        password: '',
      },
      repeat_password: ''
    };
  },
  components: {
    //ToggleButton,
    RadioForm,
    DatePick,
  },
  methods: {
    validDate(inputText) {
      var dateformat = /^(0?[1-9]|[12][0-9]|3[01])[.](0?[1-9]|1[012])[.]\d{4}$/;
      // Match the date format through regular expression
      if (inputText.match(dateformat)) {
        // Extract the string into month, date and year
        var pdate = inputText.split('.')
        var dd = parseInt(pdate[0]);
        var mm  = parseInt(pdate[1]);
        var yy = parseInt(pdate[2]);
        // Create list of days of a month [assume there is no leap year by default]
        var ListofDays = [31,28,31,30,31,30,31,31,30,31,30,31];
        if (mm==1 || mm>2) {
          if (dd>ListofDays[mm-1]) {
            return false;
          }
        }
        if (mm==2) {
          var lyear = false;
          if ( (!(yy % 4) && yy % 100) || !(yy % 400)) {
            lyear = true;
          }
          if ((lyear==false) && (dd>=29)) {
            return false;
          }
          if ((lyear==true) && (dd>29)) {
            return false;
          }
        }
      } else {
        return false;
      }
      return true;
    },
    validName(name) {
      var re = /^([A-Za-z]+[-']?)+( [A-Za-z]+[-']?)?$/
      return re.test(name)
    },
    validPassword(pswrd, repeat) {
      return pswrd===repeat
    },
    validID(id) {
      return id.length == 12
    },
    checkForm(e) {
      this.errors = new Map()
      if (!this.patient.name) {
        this.errors.set('name', "required")
      } else if (!this.validName(this.patient.name)) {
        this.errors.set('name', "not valid")
      }
      if (!this.patient.surname) {
        this.errors.set('surname', "required")
      } else if (!this.validName(this.patient.surname)) {
        this.errors.set('surname', "not valid")
      }
      if (!this.patient.middlename) {
        this.errors.set('middlename', "required")
      } else if (!this.validName(this.patient.middlename)) {
        this.errors.set('middlename', "not valid")
      }
      if (!this.patient.date) {
        this.errors.set('date', "date required.")
      } else if (!this.validDate(this.patient.date)) {
        this.errors.set('date', "not valid")
      }
      if (!this.patient.iin) {
        this.errors.set('iin', "iin required.")
      } else if (!this.validID(this.patient.iin)) {
        this.errors.set('iin', "not valid")
      }
      if (!this.patient.id) {
        this.errors.set('id', "required")
      } else if (!this.validID(this.patient.iin)) {
        this.errors.set('id', "not valid")
      }
      if (!this.patient.blood_type) {
        this.errors.set('blood_type', "required.")
      }
      if (!this.patient.marital_status) {
        this.errors.set('marital_status', "required.")
      }
      if (!this.patient.contact_number) {
        this.errors.set('contact_number', "required.")
      }
      if (!this.patient.emergency_contact_number) {
        this.errors.set('emergency_contact_number', "required.")
      }
      if (!this.patient.address) {
        this.errors.set('address', "required.")
      }
      if (!this.patient.password) {
        this.errors.set('password', "required.")
      } else if (!this.validPassword(this.patient.password, this.patient.password)) {
        this.errors.set('repeat', "does not match.")
      }

      if (!this.errors.size) {
        axios
          .put(`${server_url}/api/patient/${this.$route.params.iin}/`, this.patient, { headers: {"Authorization": 'Token ' + localStorage.access_token} })
          .then((response) => {
            alert("Success")
            console.log(response)
          })
          .catch(function (error) {
            alert("Error")
            console.log(error)
          })
        return true
      }

      e.preventDefault()
    },
  },
  mounted () {
    console.log(this.$route.params.iin)
    if (localStorage.access_token) {
      axios
        .get(`${server_url}/api/patient/${this.$route.params.iin}`, { headers: {"Authorization": 'Token ' + localStorage.access_token} })
        .then((response) => {
          console.log(response.data)
          this.patient = response.data
        })
        .catch(function (error) {
          alert("Could not load patient")
          console.log(error)
        })
    }
  }
};
</script>
