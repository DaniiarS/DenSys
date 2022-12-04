<template>
  <index-navbar />
  <div
    class="flex bg-slate-100 m-auto items-center justify-center w-screen h-screen"
  ></div>
</template>

<script>
import IndexNavbar from "@/components/IndexNavbar.vue";
export default {
  name: "radio-form",
  data() {
    return {};
  },
  model: {
    prop: "input_type",
    event: "update:input_type",
  },
  props: ["buttons", "input_type"],
  components: {
    IndexNavbar,
  },
  methods: {
    updateActive(type) {
      this.$emit("update:input_type", type);
    },
  },
};
</script>
