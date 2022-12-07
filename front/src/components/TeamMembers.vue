<template>
  <div class="pb-32">
    <div class="max-h-screen flex items-center justify-center">
      <img class="mx-auto max-w-5xl h-auto rounded-lg" :src="nulogo" />
      <img class="mx-auto max-w-5xl h-auto rounded-lg" :src="sedslogo" />
    </div>
    <div class="text-center text-4xl">
      <p class="mx-auto w-6/12">
        DenSys project was developed by Bekzat Kabdrashev, Batyrbek Mukhatbekov,
        Daniiar Suiunbekov and Yerslan Shakenov, a team of 4 undergraduate
        students studying at Nazarbayev University and majoring in Computer
        Science for the course CSCI 361 Software Engineering.
      </p>
    </div>
  </div>
</template>

<script>
import nulogo from "@/assets/img/nu-logo.png";
import sedslogo from "@/assets/img/seds-logo.png";

export default {
  data() {
    return {
      nulogo,
      sedslogo,
    };
  },
};
</script>
