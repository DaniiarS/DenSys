<template>
  <div
    class="container mx-auto h-full w-full lg:w-full flex content-center items-center justify-center h-full"
  >
    <div
      class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-slate-200 border-0"
    >
      <div class="flex-auto px-4 lg:px-10 py-10 pt-0">
        <div class="text-slate-800 text-center py-3 font-bold">
          Doctor Information
        </div>
        <hr class="pb-4 border-t-1 border-slate-300" />
        <div class="flex flex-wrap">
          <div class="w-full lg:w-4/12 px-4 inline-block relative mb-3">
            <div
              class="flex-wrap block uppercase text-slate-600 text-xs font-bold mb-2"
            >
              Name
              <div
                class="inline-block text-rose-700 fa-2xs fa-solid fa-circle"
              ></div>
              <div
                class="inline-block px-4 text-rose-700"
                v-if="errors.get('name') && !validName(doctor.name)"
              >
                {{ errors.get("name") }}
              </div>
            </div>
            <input
              type="text"
              v-model="doctor.name"
              class="w-full relative border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring ease-linear transition-all duration-150"
              :class="[
                errors.size && !validName(doctor.name)
                  ? 'border-2 border-rose-700'
                  : 'border-0',
              ]"
              placeholder="Name"
            />
          </div>
          <div class="w-full lg:w-4/12 px-4 inline-block relative mb-3">
            <label
              class="block uppercase text-slate-600 text-xs font-bold mb-2"
            >
              Surname
              <div class="text-rose-700 fa-2xs fa-solid fa-circle"></div>
              <div
                class="inline-block px-4 text-rose-700"
                v-if="errors.get('surname') && !validName(doctor.surname)"
              >
                {{ errors.get("surname") }}
              </div>
            </label>
            <input
              type="text"
              v-model="doctor.surname"
              class="w-full relative border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring ease-linear transition-all duration-150"
              :class="[
                errors.size && !validName(doctor.surname)
                  ? 'border-2 border-rose-700'
                  : 'border-0',
              ]"
              placeholder="Surname"
            />
          </div>
          <div class="w-full lg:w-4/12 px-4 inline-block relative mb-3">
            <label
              class="block uppercase text-slate-600 text-xs font-bold mb-2"
            >
              Middlename
              <div class="text-rose-700 fa-2xs fa-solid fa-circle"></div>
              <div
                class="inline-block px-4 text-rose-700"
                v-if="errors.get('middlename') && !validName(doctor.middlename)"
              >
                {{ errors.get("middlename") }}
              </div>
            </label>
            <input
              type="text"
              v-model="doctor.middlename"
              class="w-full relative border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring ease-linear transition-all duration-150"
              :class="[
                errors.size && !validName(doctor.middlename)
                  ? 'border-2 border-rose-700'
                  : 'border-0',
              ]"
              placeholder="Middlename"
            />
          </div>
          <div class="w-full lg:w-4/12 px-4 inline-block relative mb-3">
            <label
              class="block uppercase text-slate-600 text-xs font-bold mb-2"
            >
              Date of Birth
              <div class="text-slate-600 fa-2xs fa-solid fa-circle"></div>
              <div
                class="inline-block px-4 text-rose-700"
                v-if="errors.get('bddate') && !validDate(doctor.bddate)"
              >
                {{ errors.get("bddate") }}
              </div>
            </label>
            <date-pick
              v-model:value="doctor.bddate"
              :isDisabled="true"
              :selectableYearRange="{ from: 1930, to: 2022 }"
              :format="'DD.MM.YYYY'"
            />
          </div>
          <div class="w-full lg:w-4/12 px-4 inline-block relative mb-3">
            <label
              class="block uppercase text-slate-600 text-xs font-bold mb-2"
            >
              IIN number
              <div class="text-slate-600 fa-2xs fa-solid fa-circle"></div>
              <div
                class="inline-block px-4 text-rose-700"
                v-if="errors.get('iin') && !validID(doctor.iin)"
              >
                {{ errors.get("iin") }}
              </div>
            </label>
            <input
              type="text"
              v-model="doctor.iin"
              disabled
              class="border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150 disabled:text-slate-300"
              :class="[
                errors.size && !validID(doctor.iin)
                  ? 'border-2 border-rose-700'
                  : 'border-0',
              ]"
              placeholder="IIN number"
            />
          </div>
          <div class="w-full lg:w-4/12 px-4 inline-block relative mb-3">
            <label
              class="block uppercase text-slate-600 text-xs font-bold mb-2"
            >
              ID number
              <div class="text-rose-700 fa-2xs fa-solid fa-circle"></div>
              <div
                class="inline-block px-4 text-rose-700"
                v-if="errors.get('id') && !validID(doctor.id)"
              >
                {{ errors.get("id") }}
              </div>
            </label>
            <input
              type="text"
              v-model="doctor.id"
              class="border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
              :class="[
                errors.size && !validID(doctor.id)
                  ? 'border-2 border-rose-700'
                  : 'border-0',
              ]"
              oninput="this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*)\./g, '$1');"
              placeholder="id number"
            />
          </div>

          <div class="flex-auto inline-block">
            <div class="px-4 relative w-full mb-3">
              <label
                class="block uppercase text-slate-600 text-xs font-bold mb-2"
              >
                Education
                <div class="text-rose-700 fa-2xs fa-solid fa-circle"></div>
                <div
                  class="inline-block px-4 text-rose-700"
                  v-if="errors.get('education') && !doctor.education"
                >
                  {{ errors.get("education") }}
                </div>
              </label>
              <radio-form
                :class="[
                  errors.size && !doctor.education
                    ? 'border-2 border-rose-700'
                    : 'border-0',
                ]"
                :buttons="['MD', 'PhD', 'DO']"
                v-model:input_type="doctor.education"
              />
            </div>
            <div class="px-4 relative w-full mb-3">
              <label
                class="block uppercase text-slate-600 text-xs font-bold mb-2"
              >
                Deparament
                <div class="text-rose-700 fa-2xs fa-solid fa-circle"></div>
                <div
                  class="inline-block px-4 text-rose-700"
                  v-if="errors.get('departament') && !doctor.departament"
                >
                  {{ errors.get("departament") }}
                </div>
              </label>
              <radio-form
                :class="[
                  errors.size && !doctor.departament
                    ? 'border-2 border-rose-700'
                    : 'border-0',
                ]"
                :buttons="[
                  'Cardiology',
                  'Surgery',
                  'Gynecology',
                  'Neurology',
                  'Oncology',
                ]"
                v-model:input_type="doctor.departament"
              />
            </div>
            <div class="px-4 relative w-full mb-3">
              <label
                class="block uppercase text-slate-600 text-xs font-bold mb-2"
              >
                Specialization
                <div class="text-rose-700 fa-2xs fa-solid fa-circle"></div>
                <div
                  class="inline-block px-4 text-rose-700"
                  v-if="errors.get('specialization') && !doctor.specialization"
                >
                  {{ errors.get("specialization") }}
                </div>
              </label>
              <radio-form
                :class="[
                  errors.size && !doctor.specialization
                    ? 'border-2 border-rose-700'
                    : 'border-0',
                ]"
                :buttons="[
                  'General',
                  'Pediatrist',
                  'Surgeon',
                  'Oculist',
                  'Neurologist',
                ]"
                v-model:input_type="doctor.specialization"
              />
            </div>
            <div class="px-4 relative w-full mb-3">
              <label
                class="block uppercase text-slate-600 text-xs font-bold mb-2"
              >
                Category
                <div class="text-rose-700 fa-2xs fa-solid fa-circle"></div>
                <div
                  class="inline-block px-4 text-rose-700"
                  v-if="errors.get('category') && !doctor.category"
                >
                  {{ errors.get("category") }}
                </div>
              </label>
              <radio-form
                :class="[
                  errors.size && !doctor.category
                    ? 'border-2 border-rose-700'
                    : 'border-0',
                ]"
                :buttons="['Second', 'First', 'Highest', 'None']"
                v-model:input_type="doctor.category"
              />
            </div>
          </div>

          <div class="flex-none inline-block item-center px-4">
            <photo-upload
              :enableEdits="true"
              :photoDefault="defaultPhoto"
              buttonClass="bg-slate-800 text-slate-100
                         active:bg-slate-600
                         text-sm font-bold uppercase
                         px-2 py-2 mx-1 rounded
                         shadow-slate-900
                         disabled:bg-slate-600
                         disabled:shadow-none
                         shadow hover:shadow-sm
                         outline-none focus:outline-none
                         ease-linear transition-all duration-150"
              :showMessages="false"
              @photo-submit="photo_upload"
              @photo-change="photo_changed"
            />
          </div>
          <div class="w-full lg:w-4/12 px-4 inline-block relative mb-3">
            <label
              class="block uppercase text-slate-600 text-xs font-bold mb-2"
            >
              Working Hours
              <div class="text-rose-700 fa-2xs fa-solid fa-circle"></div>
              <div
                class="inline-block px-4 text-rose-700"
                v-if="errors.get('bddate') && !validDate(doctor.bddate)"
              >
                {{ errors.get("bddate") }}
              </div>
            </label>
            <week-time-pick v-model:value="doctor.working_hours" />
          </div>
          <div class="w-full lg:w-4/12 px-4 inline-block relative mb-3">
            <label
              class="block uppercase text-slate-600 text-xs font-bold mb-2"
            >
              Appointment Duration
              <div class="text-rose-700 fa-2xs fa-solid fa-circle"></div>
              <div
                class="inline-block px-4 text-rose-700"
                v-if="errors.get('duration') && !validDate(doctor.duration)"
              >
                {{ errors.get("duration") }}
              </div>
            </label>
            <input
              type="number"
              step="5"
              min="0"
              v-model="doctor.duration"
              class="border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
              :class="[
                errors.size && !doctor.duration
                  ? 'border-2 border-rose-700'
                  : 'border-0',
              ]"
              placeholder="Appointment Duration"
            />
          </div>
          <div class="w-full lg:w-4/12 px-4 inline-block relative mb-3">
            <label
              class="block uppercase text-slate-600 text-xs font-bold mb-2"
            >
              Appointment Price
              <div class="text-rose-700 fa-2xs fa-solid fa-circle"></div>
              <div
                class="inline-block px-4 text-rose-700"
                v-if="errors.get('price') && !validDate(doctor.price)"
              >
                {{ errors.get("price") }}
              </div>
            </label>
            <input
              type="number"
              step="200"
              min="0"
              v-model="doctor.price"
              class="border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
              :class="[
                errors.size && !doctor.price
                  ? 'border-2 border-rose-700'
                  : 'border-0',
              ]"
              placeholder="Appointment Price"
            />
          </div>

          <div class="w-full lg:w-6/12 px-4 inline-block relative mb-3">
            <label
              class="block uppercase text-slate-600 text-xs font-bold mb-2"
            >
              Contact Number
              <div class="text-rose-700 fa-2xs fa-solid fa-circle"></div>
              <div
                class="inline-block px-4 text-rose-700"
                v-if="errors.get('contact_number') && !doctor.contact_number"
              >
                {{ errors.get("contact_number") }}
              </div>
            </label>
            <input
              type="text"
              v-model="doctor.contact_number"
              class="border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
              :class="[
                errors.size && !doctor.contact_number
                  ? 'border-2 border-rose-700'
                  : 'border-0',
              ]"
              placeholder="Contact Number"
              oninput="this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*)\./g, '$1');"
            />
          </div>
          <div class="w-full lg:w-6/12 px-4 inline-block relative mb-3">
            <label
              class="block uppercase text-slate-600 text-xs font-bold mb-2"
            >
              Experience
              <div class="text-rose-700 fa-2xs fa-solid fa-circle"></div>
              <div
                class="inline-block px-4 text-rose-700"
                v-if="errors.get('experience') && !doctor.experience"
              >
                {{ errors.get("experience") }}
              </div>
            </label>
            <input
              type="number"
              min="0"
              v-model="doctor.experience"
              class="border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
              :class="[
                errors.size && !doctor.experience
                  ? 'border-2 border-rose-700'
                  : 'border-0',
              ]"
              @input="
                this.value = this.value
                  .replace(/[^0-9.]/g, '')
                  .replace(/(\..*)\./g, '$1')
              "
              placeholder="Experience in years"
            />
          </div>
          <div class="w-full lg:w-6/12 px-4 inline-block relative mb-3">
            <label
              class="block uppercase text-slate-600 text-xs font-bold mb-2"
            >
              Homepage URL (Optional)
            </label>
            <input
              type="email"
              v-model="doctor.homepage"
              class="border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
              placeholder="Homepage URL"
            />
          </div>
          <div class="w-full lg:w-6/12 px-4 inline-block relative mb-3">
            <label
              class="block uppercase text-slate-600 text-xs font-bold mb-2"
            >
              Address
              <div class="text-rose-700 fa-2xs fa-solid fa-circle"></div>
              <div
                class="inline-block px-4 text-rose-700"
                v-if="errors.get('address') && !doctor.address"
              >
                {{ errors.get("address") }}
              </div>
            </label>
            <input
              type="textDoctor"
              v-model="doctor.address"
              :class="[
                errors.size && !doctor.address
                  ? 'border-2 border-rose-700'
                  : 'border-0',
              ]"
              class="border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
              placeholder="Address"
            />
          </div>
          <div class="w-full text-center px-4 mt-6">
            <button
              class="bg-slate-800 text-white active:bg-slate-600 text-sm font-bold uppercase px-6 py-3 rounded mr-1 mb-1 w-full shadow hover:shadow-lg outline-none focus:outline-none ease-linear transition-all duration-150"
              @click="checkForm"
              type="button"
            >
              Update Doctor Information
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { server_url } from "@/api.js";

import RadioForm from "@/components/RadioForm.vue";
import DatePick from "@/components/vueDatePick.vue";
import PhotoUpload from "@/components/PhotoUpload.vue";
import WeekTimePick from "@/components/WeekTimePick.vue";

import blankDoctor from "@/assets/img/blankDoctor.jpg";

export default {
  name: "doctor-profile",
  data() {
    return {
      iin: "",
      defaultPhoto: blankDoctor,
      errors: new Map(),
      doctor: {
        name: "",
        surname: "",
        middlename: "",
        bddate: "",
        iin: "",
        id: "",
        education: "",
        departament: "",
        specialization: "",
        category: "",
        photo: null,
        working_hours: [[], [], [], [], [], [], []],
        duration: "",
        price: "",
        contact_number: "",
        experience: "",
        homepage: "",
        address: "",
      },
      photo: null,
    };
  },
  components: {
    RadioForm,
    DatePick,
    PhotoUpload,
    WeekTimePick,
  },
  methods: {
    photo_upload(e, file) {
      this.defaultPhoto = URL.createObjectURL(file);
      this.photo = file;
    },
    photo_changed(e, file) {
      console.log(e, file);
    },
    validDate(inputText) {
      var dateformat = /^(0?[1-9]|[12][0-9]|3[01])[.](0?[1-9]|1[012])[.]\d{4}$/;
      // Match the date format through regular expression
      if (inputText.match(dateformat)) {
        // Extract the string into month, date and year
        var pdate = inputText.split(".");
        var dd = parseInt(pdate[0]);
        var mm = parseInt(pdate[1]);
        var yy = parseInt(pdate[2]);
        // Create list of days of a month [assume there is no leap year by default]
        var ListofDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
        if (mm == 1 || mm > 2) {
          if (dd > ListofDays[mm - 1]) {
            return false;
          }
        }
        if (mm == 2) {
          var lyear = false;
          if ((!(yy % 4) && yy % 100) || !(yy % 400)) {
            lyear = true;
          }
          if (lyear == false && dd >= 29) {
            return false;
          }
          if (lyear == true && dd > 29) {
            return false;
          }
        }
      } else {
        return false;
      }
      return true;
    },
    validName(name) {
      var re = /^([A-Za-z]+[-']?)+( [A-Za-z]+[-']?)?$/;
      return re.test(name);
    },
    validPassword(password, repeat) {
      return password === repeat;
    },
    validID(id) {
      return id.length == 12;
    },
    checkForm(e) {
      this.errors = new Map();
      if (!this.doctor.name) {
        this.errors.set("name", "required");
      } else if (!this.validName(this.doctor.name)) {
        this.errors.set("name", "not valid");
      }
      if (!this.doctor.surname) {
        this.errors.set("surname", "required");
      } else if (!this.validName(this.doctor.surname)) {
        this.errors.set("surname", "not valid");
      }
      if (!this.doctor.middlename) {
        this.errors.set("middlename", "required");
      } else if (!this.validName(this.doctor.middlename)) {
        this.errors.set("middlename", "not valid");
      }
      if (!this.doctor.bddate) {
        this.errors.set("bddate", "required.");
      } else if (!this.validDate(this.doctor.bddate)) {
        this.errors.set("bddate", "not valid");
      }
      if (!this.doctor.iin) {
        this.errors.set("iin", "required.");
      } else if (!this.validID(this.doctor.iin)) {
        this.errors.set("iin", "not valid");
      }
      if (!this.doctor.id) {
        this.errors.set("id", "required");
      } else if (!this.validID(this.doctor.id)) {
        this.errors.set("id", "not valid");
      }
      if (!this.doctor.education) {
        this.errors.set("education", "required.");
      }
      if (!this.doctor.departament) {
        this.errors.set("departament", "required.");
      }
      if (!this.doctor.specialization) {
        this.errors.set("specialization", "required.");
      }
      if (!this.doctor.category) {
        this.errors.set("category", "required.");
      }
      if (!this.doctor.contact_number) {
        this.errors.set("contact_number", "required.");
      }
      if (!this.doctor.experience) {
        this.errors.set("experience", "required.");
      }
      if (!this.doctor.address) {
        this.errors.set("address", "required.");
      }

      if (!this.errors.size) {
        const formData = new FormData();
        formData.append("name", this.doctor.name);
        formData.append("surname", this.doctor.surname);
        formData.append("middlename", this.doctor.middlename);
        formData.append("bddate", this.doctor.bddate);
        formData.append("id", this.doctor.id);
        formData.append("education", this.doctor.education);
        formData.append("departament", this.doctor.departament);
        formData.append("specialization", this.doctor.specialization);
        formData.append("category", this.doctor.category);
        formData.append("contact_number", this.doctor.contact_number);
        formData.append("experience", this.doctor.experience);
        formData.append("homepage", this.doctor.homepage);
        formData.append("address", this.doctor.address);
        formData.append(
          "working_hours",
          JSON.stringify(this.doctor.working_hours)
        );
        formData.append("duration", this.doctor.duration);
        formData.append("price", this.doctor.price);
        if (this.photo) {
          formData.append("photo", this.photo);
        }
        console.log(formData);
        axios
          .put(
            `${server_url}/api/doctor/update/${this.$route.params.iin}/`,
            formData,
            {
              headers: { Authorization: "Token " + localStorage.access_token },
            },
            { headers: { "Content-Type": "multipart/form-data" } }
          )
          .then((response) => {
            alert("Success");
            console.log(response);
          })
          .catch(function (error) {
            alert("Error");
            console.log(error);
          });
        return true;
      }

      e.preventDefault();
    },
  },
  mounted() {
    console.log(this.$route.params.iin);
    console.log(localStorage.user_iin);
    this.iin = localStorage.user_iin;
    if (this.$route.params.iin) {
      this.iin = this.$route.params.iin;
    }
    if (localStorage.access_token) {
      axios
        .get(`${server_url}/api/doctor/${this.iin}`, {
          headers: { Authorization: "Token " + localStorage.access_token },
        })
        .then((response) => {
          this.doctor = response.data;
          this.defaultPhoto = server_url + this.doctor.photo;
        })
        .catch(function (error) {
          alert("Could not load Doctor");
          console.log(error);
        });
    }
  },
};
</script>
