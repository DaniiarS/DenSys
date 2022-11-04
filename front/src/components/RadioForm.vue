<template>
  <div class="flex-wrap">
    <div class="inline-flex shadow-md hover:shadow-lg focus:shadow-lg" role="group"
         v-for="(buttn,idx) in buttons" :key="idx">
      <toggle-button :toggleButtonName = "buttn" v-model:active_type="active_type"/>
    </div>
  </div>
</template>

<script>
import ToggleButton from "@/components/Cards/ToggleButton.vue"

export default {
  name: "radio-form",
  data() {
    return {
      active_type: '',
    };
  },
  props: ['buttons'],
  components: {
    ToggleButton
  },
};
</script>
