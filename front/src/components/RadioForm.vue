<template>
  <div class="flex-wrap inline-block">
    <div class="inline-flex shadow-md hover:shadow-lg focus:shadow-lg" role="group"
         v-for="(buttn,idx) in buttons" :key="idx">
      <toggle-button :toggleButtonName = "buttn" v-model:active_type="active_type" @click="updateActive"/>
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
  model: {
    prop: 'input_type',
    event: 'update:input_type'
  },
  props: ['buttons', 'input_type'],
  components: {
    ToggleButton
  },
  methods: {
    updateActive() {
      this.$emit('update:input_type', this.active_type)
    }
  }
};
</script>
