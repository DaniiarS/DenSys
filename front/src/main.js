import { createApp } from "vue";
import { createWebHistory, createRouter } from "vue-router";

// styles

import "@/output.css";
import "@fortawesome/fontawesome-free/css/all.min.css";

// mouting point for the whole app

import App from "@/App.vue";

// layouts

import Admin           from "@/layouts/AdminLayout.vue";
import AdminLogin      from "@/views/AdminLogin.vue";
import UserLogin       from "@/views/UserLogin.vue";
import Patient         from "@/layouts/PatientLayout.vue";
import Doctor          from "@/layouts/DoctorLayout.vue";
import MakeAppointment from "@/components/MakeAppointment.vue";
import ServiceRequest  from "@/components/ServiceRequest.vue";

// views for Admin layout
import PatientRegister from "@/components/PatientRegister.vue";
import ServiceRegister from "@/components/ServiceRegister.vue";
import DoctorRegister  from "@/components/DoctorRegister.vue";

import ServiceTable    from "@/components/ServicesTable.vue";
import PatientsTable   from "@/components/PatientsTable.vue";
import PatientHistory  from "@/components/PatientHistory.vue";
import DoctorsTable    from "@/components/DoctorsTable.vue";
import PatientRequests from "@/components/PatientRequests.vue";
import RequestsTable   from "@/components/RequestsTable.vue";

import AppointmentCard from "@/components/AppointmentCard.vue";
import ServiceReqCard  from "@/components/ServiceRequestCard.vue";
import MyAppointments  from "@/components/MyAppointments.vue";
import MyPatients      from "@/components/MyPatients.vue";

import PatientInfo     from "@/components/PatientProfile.vue";
import DoctorInfo      from "@/components/DoctorProfile.vue";
// views without layouts

import Index     from "@/views/IndexPage.vue";

import ContactUs   from "@/components/ContactUs.vue";
import AboutUs     from "@/components/AboutUs.vue";
import TeamMembers from "@/components/TeamMembers.vue";

const routes = [
  {
    path: "/admin",
    component: Admin,
    children: [
      { path: "/admin/patient-register",      component: PatientRegister, },
      { path: "/admin/service-register",      component: ServiceRegister, },
      { path: "/admin/service",               component: ServiceTable, },
      { path: "/admin/doctor-register",       component: DoctorRegister, },
      { path: "/admin/doctors/:iin",          component: DoctorInfo, },
      { path: "/admin/patients/:iin",         component: PatientInfo, },
      { path: "/admin/patients",              component: PatientsTable, },
      { path: "/admin/doctors",               component: DoctorsTable, },
      { path: "/admin/requests",              component: RequestsTable, },
      { path: "/admin/appointment/:aid",      component: AppointmentCard, },
      { path: "/admin/service-request/:srid", component: ServiceReqCard, },
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
      { path: "/patient/make-appointment",      component: MakeAppointment, },
      { path: "/patient/appointment/:aid",      component: AppointmentCard, },
      { path: "/patient/service-request/:srid", component: ServiceReqCard, },
      { path: "/patient/service-request",       component: ServiceRequest, },
      { path: "/patient/profile",               component: PatientInfo, },
      { path: "/patient/requests",              component: PatientRequests, },
    ],
  },
  {
    path: "/doctor",
    component: Doctor,
    children: [
      { path: "/doctor/my-patients", component: MyPatients, },
      { path: "/doctor/my-patients/:iin", component: PatientHistory, },
      { path: "/doctor/profile", component: DoctorInfo, },
      { path: "/doctor/my-appointments", component: MyAppointments, },
      { path: "/doctor/my-appointments/:aid", component: AppointmentCard, },
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
      { path: "/make-appointment", component: MakeAppointment, },
      { path: "/service-request", component: ServiceRequest, },
      { path: "/contactus", component: ContactUs, },
      { path: "/aboutus", component: AboutUs, },
      { path: "/", component: TeamMembers, },
    ],
  },
  { path: "/:pathMatch(.*)*", redirect: "/" },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

createApp(App).use(router).mount("#app");
