<template>
  <div class="overflow-hidden h-screen">
    <img class="mx-auto max-w-5xl h-auto rounded-lg" :src="hospital" />

    <div class="text-center pt-10 px-4 text-lg">
      <p class="mx-auto w-6/12">
        Cutting-edge medicine based on excellent management structures. The
        Hospital Advisory Board (the chief management body), Hospital Executive
        Board (operative decision-making body) and eight departmental and
        trans-sectoral directorates are jointly responsible for the Hospital
        Densys. {{ doctor }} doctors work in this hospital and treat thousands
        of patients every year.
      </p>
    </div>
  </div>
</template>

<script>
import hospital from "@/assets/img/hospital.jpeg";

export default {
  data() {
    return {
      hospital,
      doctor: 40,
    };
  },
};
</script>
