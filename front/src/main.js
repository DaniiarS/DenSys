import { createApp } from "vue";
import { createWebHistory, createRouter } from "vue-router";

// styles

import "@/output.css";
import "@fortawesome/fontawesome-free/css/all.min.css";

// mouting point for the whole app

import App from "@/App.vue";

// layouts

import Admin              from "@/layouts/AdminLayout.vue";
import AdminLogin         from "@/views/AdminLogin.vue";
import UserLogin          from "@/views/UserLogin.vue";
import Patient            from "@/layouts/PatientLayout.vue";
import MakeAppointment    from "@/components/MakeAppointment.vue";

// views for Admin layout

import PatientRegister from "@/components/PatientRegister.vue";
import DoctorRegister  from "@/components/DoctorRegister.vue";

import PatientsTable   from "@/components/PatientsTable.vue";
import DoctorsTable    from "@/components/DoctorsTable.vue";

import PatientProfile  from "@/components/PatientProfile.vue";
import DoctorProfile   from "@/components/DoctorProfile.vue";
// views without layouts

import Index from "@/views/IndexPage.vue";


// routes

const routes = [
  {
    path: "/admin",
    component: Admin,
    children: [
      {
        path: "/admin/patient-register",
        component: PatientRegister,
      },
      {
        path: "/admin/doctor-register",
        component: DoctorRegister
      },
      {
        path: "/admin/doctors/:iin",
        component: DoctorProfile,
      },
      {
        path: "/admin/patients/:iin",
        component: PatientProfile,
      },
      {
        path: "/admin/patients",
        component: PatientsTable,
      },
      {
        path: "/admin/doctors",
        component: DoctorsTable,
      },
    ],
  },
  {
    path: "/admin/login",
    component: AdminLogin,
  },
  {
    path: "/patient",
    component: Patient,
    children: [
      {
        path: "/patient/make-appointment",
        component: MakeAppointment,
      },
      {
        path: "/patient/profile",
        component: PatientProfile,
      },
    ],
  },
  {
    path: "/login",
    component: UserLogin,
  },
  {
    path: "/",
    component: Index,
  },
  { path: "/:pathMatch(.*)*", redirect: "/" },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

createApp(App).use(router).mount("#app");
