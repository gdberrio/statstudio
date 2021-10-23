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
import axios from 'axios';

export default {
  data() {
    return {
      file: null,
      data: null
    }
  },
  methods: {
    Import() {
      var reader = new FileReader();
      reader.readAsText(this.file);
      reader.onload = () => {
        const content_data = reader.result.split('\n');
        const header = content_data[0];
        const cols = header.split(',');
        content_data.shift();
        var file_json = {};
        for (var i = 0; i < cols.length; i++) {
          file_json[cols[i]] = Object.assign({}, content_data.map(x => x.split(',')[i]));
          file_json[cols[i]] = Object.assign({}, content_data.map(x => x.split(',')[i]));  
        }            
        var data = JSON.stringify(file_json);

        axios.post(
          'http://127.0.0.1:8000/count_data/predict/',
          data,
          {
            headers: {
            'Content-Type': 'application/json'
            },
          }
        ).then(response => {
          console.log(response);
        });
      }      
    }
  }
}
</script>
