<template>
  <v-container>
    <v-file-input
      counter
      show-size
      accept="text/csv"
      label="file input"
      placeholder="select csv to upload"
      v-model="file"
    >
    </v-file-input>
    <v-spacer></v-spacer>
    <v-btn right @click="Import">Upload</v-btn>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      file: null,
      data: null,
    }
  },
  methods: {
    Import() {
      var reader = new FileReader();
      reader.readAsText(this.file);
      reader.onload = () => {
        this.data = reader.result;
      }
    }
  }
}
</script>
