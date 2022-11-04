<template>
  <div class="container mx-auto px-4 h-full">
    <div class="flex content-center items-center justify-center h-full">
      <div class="w-full lg:w-full px-4">
        <div class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-slate-200 border-0">
          <div class="flex-auto px-4 lg:px-10 py-10 pt-0">
            <div class="text-slate-400 text-center py-3 font-bold">
              Patient Registration Form
            </div>
            <div class="flex-wrap">
              <div class="w-full lg:w-4/12 px-4 inline-block relative mb-3">
                <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
                  Name
                </label>
                <input type="text"
                       class="w-full relative border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring ease-linear transition-all duration-150"
                       placeholder="Name"/>

              </div>
              <div class="w-full lg:w-4/12 px-4 inline-block relative mb-3">
                <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
                  Surname
                </label>
                <input type="text"
                       class="w-full relative border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring ease-linear transition-all duration-150"
                       placeholder="Surname"/>
              </div>
              <div class="w-full lg:w-4/12 px-4 inline-block relative mb-3">
                <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
                  Middlename
                </label>
                <input type="text"
                       class="w-full relative border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring ease-linear transition-all duration-150"
                       placeholder="Middlename"/>
              </div>
              <div class="w-full lg:w-6/12 px-4 inline-block relative mb-3">
                <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
                  IIN number
                </label>
                <input type="text"
                       class="border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                       oninput="this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*)\./g, '$1');"
                       placeholder="IIN number"/>
              </div>
              <div class="w-full lg:w-6/12 px-4 inline-block relative mb-3">
                <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
                  ID number
                </label>
                <input type="text"
                       class="border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                       oninput="this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*)\./g, '$1');"
                       placeholder="IIN number"/>
              </div>
              <div class="px-4 relative w-full mb-3">
                <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
                  Blood Group
                </label>
                <radio-form :buttons="['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']"/>
              </div>
              <div class="px-4 relative w-full mb-3">
                <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
                  Marital Status
                </label>
                <radio-form :buttons="['Married', 'Single', 'Divorced', 'Widowed']"/>
              </div>

              <div class="w-full lg:w-6/12 px-4 inline-block relative mb-3">
                <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
                  Contact Number
                </label>
                <input type="email"
                       class="border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                       placeholder="Contact Number"
                       oninput="this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*)\./g, '$1');" />
              </div>
              <div class="w-full lg:w-6/12 px-4 inline-block relative mb-3">
                <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
                  Emergency Contact Number
                </label>
                <input type="email"
                       class="border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                       oninput="this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*)\./g, '$1');"
                       placeholder="Emergency Contact Number"/>
              </div>
              <div class="w-full lg:w-6/12 px-4 inline-block relative mb-3">
                <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
                  Email (Optional)
                </label>
                <input type="email"
                       class="border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                       placeholder="Email"/>
              </div>
              <div class="w-full lg:w-6/12 px-4 inline-block relative mb-3">
                <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
                  Address
                </label>
                <input type="email"
                       class="border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                       placeholder="Address"/>
              </div>
              <div class="w-full lg:w-6/12 px-4 inline-block relative mb-3">
                <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
                  Password
                </label>
                <input type="password"
                       class="border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                       placeholder="Password"/>
              </div>
              <div class="w-full lg:w-6/12 px-4 inline-block relative mb-3">
                <label class="block uppercase text-slate-600 text-xs font-bold mb-2">
                  Repeat Password
                </label>
                <input type="password"
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
                        type="button">
                  Register A New Patient
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
//import ToggleButton from "@/components/Cards/ToggleButton.vue"
import RadioForm from "@/components/RadioForm.vue"

export default {
  name: "patient-register",
  data() {
    return {
      patient_reg: {
        name: 'One',
        surname: 'Two',
        middlename: 'Three',
        IIN: '011006550214',
        blood_type: 'O+',
        marital_status: 'Married',
        contact_number: '87759232192',
        emergency_contact_number: '87759232192',
        email: 'b.k@me.com',
        address: 'Here street Astana city',
        password: '1234512345',
      },
    };
  },
  methods: {
    updateBloudGroup(bloud_group) {
      this.patient_reg.bloud_group = bloud_group
      console.log(bloud_group)
    }
  },
  components: {
    //ToggleButton,
    RadioForm
  },
};
</script>
