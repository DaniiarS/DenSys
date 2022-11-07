<template>
  <div class="container mx-auto h-full flex content-center items-center justify-center w-full lg:w-full">
    <div class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-slate-200 border-0">
      <div class="flex-auto px-4 lg:px-10 py-10 pt-0">
        <div class="text-slate-800 text-center py-3 font-bold">
          Doctor Registration Form
        </div>
        <hr class="pb-4 border-t-1 border-slate-300" />
        <div class="flex-wrap">
          <div class="w-full lg:w-4/12 px-4 inline-block relative mb-3">
            <div class="flex-wrap block uppercase text-slate-600 text-xs font-bold mb-2">
              Name <div class="inline-block text-rose-700 fa-2xs fa-solid fa-circle"></div>
              <div class="inline-block px-4 text-rose-700"
                   v-if="errors.get('name') && !validName(doctor_reg.name)">
                {{errors.get('name')}}
              </div>
            </div>
            <input type="text"
                   v-model="doctor_reg.name"
                   class="w-full relative border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring ease-linear transition-all duration-150"
                   :class="[errors.size && !validName(doctor_reg.name) ? 'border-2 border-rose-700' : 'border-0' ]"
                   placeholder="Name"/>

          </div>
          <div class="w-full lg:w-4/12 px-4 inline-block relative mb-3">
            <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
              Surname <div class="text-rose-700 fa-2xs fa-solid fa-circle"></div>
              <div class="inline-block px-4 text-rose-700"
                   v-if="errors.get('surname') && !validName(doctor_reg.surname)">
                {{errors.get('surname')}}
              </div>
            </label>
            <input type="text"
                   v-model="doctor_reg.surname"
                   class="w-full relative border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring ease-linear transition-all duration-150"
                   :class="[errors.size && !validName(doctor_reg.surname) ? 'border-2 border-rose-700' : 'border-0' ]"
                   placeholder="Surname"/>
          </div>
          <div class="w-full lg:w-4/12 px-4 inline-block relative mb-3">
            <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
              Middlename <div class="text-rose-700 fa-2xs fa-solid fa-circle"></div>
              <div class="inline-block px-4 text-rose-700"
                   v-if="errors.get('middlename') && !validName(doctor_reg.middlename)">
                {{errors.get('middlename')}}
              </div>
            </label>
            <input type="text"
                   v-model="doctor_reg.middlename"
                   class="w-full relative border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring ease-linear transition-all duration-150"
                   :class="[errors.size && !validName(doctor_reg.middlename) ? 'border-2 border-rose-700' : 'border-0' ]"
                   placeholder="Middlename"/>
          </div>
          <div class="w-full lg:w-4/12 px-4 inline-block relative mb-3">
            <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
              Date of Birth<div class="text-rose-700 fa-2xs fa-solid fa-circle"></div>
              <div class="inline-block px-4 text-rose-700"
                   v-if="errors.get('date') && !validDate(doctor_reg.date)">
                {{errors.get('date')}}
              </div>
            </label>
            <date-pick v-model:value="doctor_reg.date"
                       :selectableYearRange="{from: 1930, to: 2022}"
                       :format="'DD.MM.YYYY'"/>
          </div>
          <div class="w-full lg:w-4/12 px-4 inline-block relative mb-3">
            <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
              IIN number <div class="text-rose-700 fa-2xs fa-solid fa-circle"></div>
              <div class="inline-block px-4 text-rose-700"
                   v-if="errors.get('iin') && !validID(doctor_reg.iin)">
                {{errors.get('iin')}}
              </div>
            </label>
            <input type="text"
                   v-model="doctor_reg.iin"
                   class="border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                   :class="[errors.size && !validID(doctor_reg.iin) ? 'border-2 border-rose-700' : 'border-0' ]"
                   oninput="this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*)\./g, '$1');"
                   placeholder="IIN number"/>
          </div>
          <div class="w-full lg:w-4/12 px-4 inline-block relative mb-3">
            <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
              ID number <div class="text-rose-700 fa-2xs fa-solid fa-circle"></div>
              <div class="inline-block px-4 text-rose-700"
                   v-if="errors.get('id') && !validID(doctor_reg.id)">
                {{errors.get('id')}}
              </div>
            </label>
            <input type="text"
                   v-model="doctor_reg.id"
                   class="border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                   :class="[errors.size && !validID(doctor_reg.id) ? 'border-2 border-rose-700' : 'border-0' ]"
                   oninput="this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*)\./g, '$1');"
                   placeholder="id number"/>
          </div>
          <div class="w-full lg:w-8/12 inline-block">
          <div class="px-4 relative w-full mb-3">
            <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
              Education <div class="text-rose-700 fa-2xs fa-solid fa-circle"></div>
              <div class="inline-block px-4 text-rose-700"
                   v-if="errors.get('education') && !(doctor_reg.education)">
                {{errors.get('education')}}
              </div>
            </label>
            <radio-form :class="[errors.size && !doctor_reg.education ? 'border-2 border-rose-700' : 'border-0' ]" :buttons="['MD', 'PhD', 'DO']" v-model:input_type="doctor_reg.education"/>
          </div>
          <div class="px-4 relative w-full mb-3">
            <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
              Deparament <div class="text-rose-700 fa-2xs fa-solid fa-circle"></div>
              <div class="inline-block px-4 text-rose-700"
                   v-if="errors.get('departament') && !(doctor_reg.departament)">
                {{errors.get('departament')}}
              </div>
            </label>
            <radio-form :class="[errors.size && !doctor_reg.departament ? 'border-2 border-rose-700' : 'border-0' ]" :buttons="['Cardiology', 'Surgery', 'Gynecology', 'Neurology', 'Oncology']" v-model:input_type="doctor_reg.departament"/>
          </div>
          <div class="px-4 relative w-full mb-3">
            <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
              Specialization <div class="text-rose-700 fa-2xs fa-solid fa-circle"></div>
              <div class="inline-block px-4 text-rose-700"
                   v-if="errors.get('specialization') && !(doctor_reg.specialization)">
                {{errors.get('specialization')}}
              </div>
            </label>
            <radio-form :class="[errors.size && !doctor_reg.specialization ? 'border-2 border-rose-700' : 'border-0' ]" :buttons="['General','Pediatrist', 'Surgeon', 'Oculist', 'Neurologist']" v-model:input_type="doctor_reg.specialization"/>
          </div>
          <div class="px-4 relative w-full mb-3">
            <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
              Category <div class="text-rose-700 fa-2xs fa-solid fa-circle"></div>
              <div class="inline-block px-4 text-rose-700"
                   v-if="errors.get('category') && !(doctor_reg.category)">
                {{errors.get('category')}}
              </div>
            </label>
            <radio-form
              :class="[errors.size && !doctor_reg.category ? 'border-2 border-rose-700' : 'border-0' ]"
              :buttons="['Second', 'First', 'Highest', 'None']"
              v-model:input_type="doctor_reg.category"/>
          </div>
        </div>
        <div class="w-full lg:w-4/12 inline-block item-center px-4">
        <photo-upload
          :enableEdits="true"
          :photoDefault="defaultPhoto"
          buttonClass="bg-slate-800 text-slate-100
                       active:bg-slate-600
                       text-sm font-bold uppercase
                       px-4 py-2 mx-3 rounded
                       shadow-slate-900
                       disabled:bg-slate-600
                       disabled:shadow-none
                       shadow hover:shadow-sm
                       outline-none focus:outline-none
                       ease-linear transition-all duration-150"
          :showMessages="false"
          @photo-submit="photo_upload"
          @photo-change="photo_changed"/>
        </div>

        <div class="w-full lg:w-6/12 px-4 inline-block relative mb-3">
            <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
              Contact Number <div class="text-rose-700 fa-2xs fa-solid fa-circle"></div>
              <div class="inline-block px-4 text-rose-700"
                   v-if="errors.get('contact_number') && !(doctor_reg.contact_number)">
                {{errors.get('contact_number')}}
              </div>
            </label>
            <input type="text"
                   v-model="doctor_reg.contact_number"
                   class="border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                   :class="[errors.size && !(doctor_reg.contact_number) ? 'border-2 border-rose-700' : 'border-0' ]"
                   placeholder="Contact Number"
                   oninput="this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*)\./g, '$1');" />
          </div>
          <div class="w-full lg:w-6/12 px-4 inline-block relative mb-3">
            <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
              Experience <div class="text-rose-700 fa-2xs fa-solid fa-circle"></div>
              <div class="inline-block px-4 text-rose-700"
                   v-if="errors.get('experience') && !(doctor_reg.experience)">
                {{errors.get('experience')}}
              </div>
            </label>
            <input type="number"
                   min="0"
                   v-model="doctor_reg.experience"
                   class="border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                   :class="[errors.size && !(doctor_reg.experience) ? 'border-2 border-rose-700' : 'border-0' ]"
                   placeholder="Experience in years"/>
          </div>
          <div class="w-full lg:w-6/12 px-4 inline-block relative mb-3">
            <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
              Homepage URL (Optional)
            </label>
            <input type="email"
                   v-model="doctor_reg.homepage"
                   class="border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                   placeholder="Homepage URL"/>
          </div>
          <div class="w-full lg:w-6/12 px-4 inline-block relative mb-3">
            <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
              Address <div class="text-rose-700 fa-2xs fa-solid fa-circle"></div>
              <div class="inline-block px-4 text-rose-700"
                   v-if="errors.get('address') && !(doctor_reg.address)">
                {{errors.get('address')}}
              </div>
            </label>
            <input type="textDoctor"
                   v-model="doctor_reg.address"
                   :class="[errors.size && !doctor_reg.address ? 'border-2 border-rose-700' : 'border-0' ]"
                   class="border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                   placeholder="Address"/>
          </div>
          <div class="w-full lg:w-6/12 px-4 inline-block relative mb-3">
            <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
              Password <div class="text-rose-700 fa-2xs fa-solid fa-circle"></div>
              <div class="inline-block px-4 text-rose-700"
                   v-if="errors.get('password') && (!doctor_reg.password || doctor_reg.password !== repeat_password)">
                {{errors.get('password')}}
              </div>
            </label>
            <input type="password"
                   v-model="doctor_reg.password"
                   :class="[errors.size && (!doctor_reg.password || doctor_reg.password !== repeat_password) ? 'border-2 border-rose-700' : 'border-0' ]"
                   class="border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                   placeholder="Password"/>
          </div>
          <div class="w-full lg:w-6/12 px-4 inline-block relative mb-3">
            <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
              Repeat Password <div class="text-rose-700 fa-2xs fa-solid fa-circle"></div>
              <div class="inline-block px-4 text-rose-700"
                   v-if="errors.get('repeat') && doctor_reg.password !== repeat_password">
                {{errors.get('repeat')}}
              </div>
            </label>
            <input type="password"
                   v-model="repeat_password"
                   :class="[errors.size && !validPassword(doctor_reg.password, repeat_password) ? 'border-2 border-rose-700' : 'border-0' ]"
                   class="border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                   placeholder="Password"/>
          </div>

          <div class="text-center px-4 mt-6" >
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
              Register A New Doctor
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import axios from 'axios'
import RadioForm from "@/components/RadioForm.vue"
import DatePick from '@/components/vueDatePick.vue';
import PhotoUpload from '@/components/PhotoUpload.vue';

import blankDoctor from "@/assets/img/blankDoctor.jpg";

export default {
  name: "doctor-register",
  data() {
    return {
      defaultPhoto: blankDoctor,
      errors: new Map(),
      doctor_reg: {
        name: 'One',
        surname: 'Two',
        middlename: 'Three',
        date: '06.10.2001',
        iin: '',
        id: '123456789123',
        education: 'PhD',
        departament: 'Surgery',
        specialization: 'Surgeon',
        category: 'Second',
        contact_number: '87010001122',
        experience: '10',
        homepage: '',
        address: 'Astana, Here street',
        password: '12345',
      },
      photo: null,
      repeat_password: '12345'
    };
  },
  components: {
    PhotoUpload,
    RadioForm,
    DatePick,
  },
  methods: {
    photo_upload(e, file){
      this.defaultPhoto = URL.createObjectURL(file)
      this.photo = file
      console.log(e,file)
    },
    photo_changed(e, file){
      console.log(e,file)
    },
    uploadImage(e) {
      const file = e.target.files[0]
      this.item.image = file
      this.item.imageUrl = URL.createObjectURL(file)
    },
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
    validPassword(password, repeat) {
      return password===repeat
    },
    validID(id) {
      return id.length == 12
    },
    checkForm(e) {
      this.errors = new Map()
      if (!this.doctor_reg.name) {
        this.errors.set('name', "required")
      } else if (!this.validName(this.doctor_reg.name)) {
        this.errors.set('name', "not valid")
      }
      if (!this.doctor_reg.surname) {
        this.errors.set('surname', "required")
      } else if (!this.validName(this.doctor_reg.surname)) {
        this.errors.set('surname', "not valid")
      }
      if (!this.doctor_reg.middlename) {
        this.errors.set('middlename', "required")
      } else if (!this.validName(this.doctor_reg.middlename)) {
        this.errors.set('middlename', "not valid")
      }
      if (!this.doctor_reg.date) {
        this.errors.set('date', "date required.")
      } else if (!this.validDate(this.doctor_reg.date)) {
        this.errors.set('date', "not valid")
      }
      if (!this.doctor_reg.iin) {
        this.errors.set('iin', "IIN required.")
      } else if (!this.validID(this.doctor_reg.iin)) {
        this.errors.set('iin', "not valid")
      }
      if (!this.doctor_reg.id) {
        this.errors.set('id', "required")
      } else if (!this.validID(this.doctor_reg.id)) {
        this.errors.set('id', "not valid")
      }
      if (!this.doctor_reg.education) {
        this.errors.set('education', "required.")
      }
      if (!this.doctor_reg.departament) {
        this.errors.set('departament', "required.")
      }
      if (!this.doctor_reg.specialization) {
        this.errors.set('specialization', "required.")
      }
      if (!this.doctor_reg.category) {
        this.errors.set('category', "required.")
      }
      if (!this.doctor_reg.contact_number) {
        this.errors.set('contact_number', "required.")
      }
      if (!this.doctor_reg.experience) {
        this.errors.set('experience', "required.")
      }
      if (!this.doctor_reg.address) {
        this.errors.set('address', "required.")
      }
      if (!this.doctor_reg.password) {
        this.errors.set('password', "required.")
      } else if (!this.validPassword(this.doctor_reg.password, this.repeat_password)) {
        this.errors.set('repeat', "does not match.")
      }

      if (!this.errors.size) {
        const formData = new FormData()
        formData.append("name", this.doctor_reg.name)
        formData.append("surname", this.doctor_reg.surname)
        formData.append("middlename", this.doctor_reg.middlename)
        formData.append("date", this.doctor_reg.date)
        formData.append("iin", this.doctor_reg.iin)
        formData.append("id", this.doctor_reg.id)
        formData.append("education", this.doctor_reg.education)
        formData.append("departament", this.doctor_reg.departament)
        formData.append("specialization", this.doctor_reg.specialization)
        formData.append("category", this.doctor_reg.category)
        formData.append("contact_number", this.doctor_reg.contact_number)
        formData.append("experience", this.doctor_reg.experience)
        formData.append("homepage", this.doctor_reg.homepage)
        formData.append("address", this.doctor_reg.address)
        formData.append("password", this.doctor_reg.password)
        formData.append("photo", this.photo)
        console.log(formData)
        axios
          .post('http://localhost:8000/api/doctors/',
            formData,
            { headers: {"Content-Type": "multipart/form-data"} })
          .then((response) => {
            alert("Success")
            console.log(response)
          })
          .catch(function (error) {
            alert("Fail")
            console.log(error)
          })
        return true
      }

      e.preventDefault()
    },
  }
};
</script>
