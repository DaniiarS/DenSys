import { createApp } from "vue";
import { createWebHistory, createRouter } from "vue-router";

// styles

import "@/output.css";
import "@fortawesome/fontawesome-free/css/all.min.css";

// mouting point for the whole app

import App from "@/App.vue";

// layouts

import Admin from "@/layouts/AdminLayout.vue";
import AdminLogin from "@/views/AdminLogin.vue";
import UserLogin from "@/views/UserLogin.vue";
import Patient from "@/layouts/PatientLayout.vue";
import Doctor from "@/layouts/DoctorLayout.vue";
import MakeAppointment from "@/components/MakeAppointment.vue";

// views for Admin layout

import PatientRegister from "@/components/PatientRegister.vue";
import DoctorRegister from "@/components/DoctorRegister.vue";

import PatientsTable from "@/components/PatientsTable.vue";
import Appointments from "@/components/AppointmentTable.vue";
import DoctorsTable from "@/components/DoctorsTable.vue";

import PatientInfo from "@/components/PatientProfile.vue";
import DoctorInfo from "@/components/DoctorProfile.vue";
// views without layouts

import Index from "@/views/IndexPage.vue";

import ContactUs from "@/components/ContactUs.vue";
import AboutUs from "@/components/AboutUs.vue";
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
        component: DoctorRegister,
      },
      {
        path: "/admin/doctors/:iin",
        component: DoctorInfo,
      },
      {
        path: "/admin/patients/:iin",
        component: PatientInfo,
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
        component: PatientInfo,
      },
      {
        path: "/patient/appointments",
        component: Appointments,
      },
    ],
  },
  {
    path: "/doctor",
    component: Doctor,
    children: [
      {
        path: "/doctor/my-patients",
        component: DoctorInfo,
      },
      {
        path: "/doctor/profile",
        component: DoctorInfo,
      },
      {
        path: "/doctor/my-appointments",
        component: DoctorInfo,
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
    children: [
      {
        path: "/make-appointment",
        component: MakeAppointment,
      },
      {
        path: "/contactus",
        component: ContactUs,
      },
      {
        path: "/aboutus",
        component: AboutUs,
      },
    ],
  },
  { path: "/:pathMatch(.*)*", redirect: "/" },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

createApp(App).use(router).mount("#app");
