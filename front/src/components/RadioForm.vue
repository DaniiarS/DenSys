<template>
  <div class="flex flex-wrap inline-block">
    <div class=" flex-1 shadow-md hover:shadow-lg focus:shadow-lg" role="group"
         v-for="(buttn,idx) in buttons" :key="idx">
      <toggle-button :aactive="input_type===buttn" :toggleButtonName = "buttn" @toggle="updateActive"/>
    </div>
  </div>
</template>

<script>
import ToggleButton from "@/components/ToggleButton.vue"

export default {
  name: "radio-form",
  data() {
    return {
    };
  },
  model: {
    prop: 'input_type',
    event: 'update:input_type'
  },
  props: ['buttons', 'input_type'],
  components: {
    ToggleButton
  },
  methods: {
    updateActive(type) {
      this.$emit('update:input_type', type)
    }
  }
};
</script>
