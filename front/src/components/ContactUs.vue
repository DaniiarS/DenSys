<template>
  <div class="overflow-hidden h-screen">
    <img class="mx-auto max-w-5xl h-auto rounded-lg" :src="doctor_patient" />

    <div class="text-center pt-10 px-4 text-lg">
      <a class="text-slate-400">Contact Number: </a>
      <a class="text-slate-800 font-bold">+7-(777)-666-55-55</a>
    </div>
    <div class="text-center pt-4 px-4 text-lg">
      <a class="text-slate-400">Address: </a>
      <a class="text-slate-800 font-bold">Astana, Kabanbay Batyr Ave. 53</a>
    </div>
    <div class="text-center pt-4 px-4 text-lg">
      <a class="text-slate-400">Email: </a>
      <a class="text-slate-800 font-bold">contact@densys.med</a>
    </div>
  </div>
</template>

<script>
import doctor_patient from "@/assets/img/doctor-patient.webp";

export default {
  data() {
    return {
      doctor_patient,
    };
  },
};
</script>
