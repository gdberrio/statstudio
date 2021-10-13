<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        StatStudio
      </div>

      <v-spacer></v-spacer>

      
    </v-app-bar>

    <v-main>
      <Upload/>
    </v-main>
  </v-app>
</template>

<script>
import Upload from './components/Upload.vue';

export default {
  name: 'App',

  components: {
    Upload,
  },

  data: () => ({
    //
  }),
};
</script>
