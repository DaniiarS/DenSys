<template>
    <div class="container mx-auto h-full flex content-center items-center justify-center w-full lg:w-full">
      <div class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-slate-200 border-0">
        <div class="flex flex-col px-4 lg:px-10 py-10 pt-0">
          <div class="text-slate-800 text-center py-3 font-bold">
            Service Registration Form
          </div>
          <hr class="pb-4 border-t-1 border-slate-300" />

          <div class="flex flex-wrap">
            <div class="w-full lg:w-4/12 px-4 inline-block relative mb-3">
              <div class="flex-wrap block uppercase text-slate-600 text-xs font-bold mb-2">
                Name <div class="inline-block text-rose-700 fa-2xs fa-solid fa-circle"></div>
                <div class="inline-block px-4 text-rose-700"
                     v-if="errors.get('name') && !validName(service.name)">
                  {{errors.get('name')}}
                </div>
              </div>
              <input type="text"
                     v-model="service.name"
                     class="w-full relative border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring ease-linear transition-all duration-150"
                     :class="[errors.size && !validName(service.name) ? 'border-2 border-rose-700' : 'border-0' ]"
                     placeholder="Service Name"/>
            </div>

            <div class="px-4 relative w-full mb-3">
              <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
                Department <div class="text-rose-700 fa-2xs fa-solid fa-circle"></div>
                <div class="inline-block px-4 text-rose-700"
                     v-if="errors.get('department') && !(service.department)">
                  {{errors.get('department')}}
                </div>
              </label>
              <radio-form :class="[errors.size && !service.department ? 'border-2 border-rose-700' : 'border-0' ]" :buttons="['Surgery','Gynecology', 'Obstetrics', 'Pediatrics', 'Radiology', 'Eye', 'ENT', 'Dental', 'Orthopedics', 'Neurology', 'Cardiology', 'Psychiatry', 'Skin']" v-model:input_type="service.department"/>
            </div>

          <div class="w-full lg:w-4/12 px-4 inline-block relative mb-3">
            <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
              Working Hours <div class="text-rose-700 fa-2xs fa-solid fa-circle"></div>
              <div class="inline-block px-4 text-rose-700" v-if="errors.get('bddate') && !validDate(service.bddate)">
                {{errors.get('bddate')}}
              </div>
            </label>
            <week-time-pick v-model:value="service.working_hours"/>
          </div>

          <div class="w-full lg:w-4/12 px-4 inline-block relative mb-3">
            <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
              Service Duration <div class="text-rose-700 fa-2xs fa-solid fa-circle"></div>
              <div class="inline-block px-4 text-rose-700" v-if="errors.get('duration') && !validDate(service.duration)">
                {{errors.get('duration')}}
              </div>
            </label>
            <input type="number"
                   step="5" min="0"
                   v-model="service.duration"
                   class="border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                   :class="[errors.size && !(service.duration) ? 'border-2 border-rose-700' : 'border-0' ]"
                   placeholder="Service Duration"
                   />
          </div>
          <div class="w-full lg:w-4/12 px-4 inline-block relative mb-3">
            <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
              Service Price <div class="text-rose-700 fa-2xs fa-solid fa-circle"></div>
              <div class="inline-block px-4 text-rose-700" v-if="errors.get('price') && !validDate(service.price)">
                {{errors.get('price')}}
              </div>
            </label>
            <input type="number"
                   step="200" min="0"
                   v-model="service.price"
                   class="border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                   :class="[errors.size && !(service.price) ? 'border-2 border-rose-700' : 'border-0' ]"
                   placeholder="Service Price"
                   />
          </div>

            <div class="w-full text-center px-4 mt-6" >
              <button class="bg-slate-800 text-slate-100
                             active:bg-slate-600
                             text-sm font-bold uppercase
                             px-6 py-3 rounded mr-1 mb-1 w-full
                             shadow hover:shadow-sm
                             shadow-slate-900
                             outline-none focus:outline-none
                             ease-linear transition-all duration-150"
                      @click="checkForm"
                      type="button">
                Update Service
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>


  <script>
  import axios        from 'axios'
  import {server_url} from '@/api.js'

  import RadioForm    from "@/components/RadioForm.vue";
  import WeekTimePick from '@/components/WeekTimePick.vue';

  export default {

    data() {
      return {
        errors: new Map(),
        service: {
          name: '',
          department: '',
          price:    '',
          duration:  '',
          working_hours: [
            ['00:00 - 10:00'],
            ['00:00 - 10:00'],
            ['00:00 - 10:00'],
            ['00:00 - 10:00'],
            ['00:00 - 10:00'],
            [],
            ['00:00 - 19:00'],
          ],
        },
      };
    },

    components: {
      RadioForm,
      WeekTimePick,

    },

    methods: {
      validName(name) {
        var re = /^([A-Za-z]+[-']?)+( [A-Za-z]+[-']?)?$/
        return re.test(name)
      },
      validID(id) {
        return id.length == 12
      },
      checkForm(e) {
        this.errors = new Map()
        if (!this.service.name) {
          this.errors.set('name', "required")
        }

        if (!this.service.department) {
          this.errors.set('department', "required.")
        }

        if (!this.errors.size) {
          if (localStorage.access_token) {
            const formData = new FormData()

            formData.append("name", this.service.name)
            formData.append("department", this.service.department)
            formData.append("working_hours", JSON.stringify(this.service.working_hours))
            formData.append("price", this.service.price)
            formData.append("duration", this.service.duration)

            console.log(formData)
            console.log(localStorage.access_token)
            axios
              .put(server_url+'/api/service/update/' + this.service.id+'/',
                formData,
                { headers: {"Authorization": 'Token ' + localStorage.access_token, "Content-Type": "multipart/form-data"} })
              .then((response) => {
                alert("Success")
                console.log(response)
              })
              .catch(function (error) {
                alert("Fail")
                console.log(error)
              })
          }
          return true
        }

        e.preventDefault()
      },
    },
    mounted () {
      const sid = this.$route.params.sid
      if (localStorage.access_token) {
        axios
          .get(`${server_url}/api/service/${sid}`, { headers: {"Authorization": 'Token ' + localStorage.access_token} })
          .then((response) => {
            console.log(response.data)
            this.service = response.data
          })
          .catch(function (error) {
            alert("Could not load service")
            console.log(error)
          })
      }
    }
  };
  </script>

