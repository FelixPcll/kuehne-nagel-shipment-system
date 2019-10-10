<template>
  <div class="card-holder">
    <div class="search">
      <input type="text" placeholder="Insert the track code here..." v-model="trackRef" />
      <button @click="search()">Search</button>
    </div>
    <div class="display-info">
      <div class="info-block">
        <p>Country of dispatch:</p>
        <span class="accent">{{ item.from_coutry }}</span>
      </div>
      <div class="info-block">
        <p>Country of destination:</p>
        <span class="accent">{{ item.to_country }}</span>
      </div>
      <div class="info-block">
        <p>Package weight (kg):</p>
        <span class="accent">{{ item.package_weight }}</span>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data: () => {
    return {
      trackRef: null,
      item: {
        from_coutry: " ",
        to_country: " ",
        package_weight: " "
      }
    };
  },

  methods: {
    search() {
      let path = `http://localhost:8000/api/v0.1/shipment/?track_ref=${this.trackRef}`;
      axios
        .get(path)
        .then(response => {
          this.item = response.data[0];
          this.displayInfo();
        })
        .catch(e => {
          console.log(e);
        });
    },

    displayInfo() {
      let pkg = this.item;

      console.log(pkg);
    }
  },

  mounted() {}
};
</script>

<style lang="scss" scoped>
@import "@/main.scss";

.card-holder {
  //height: 400px;
  width: 400px;
  padding: 10px;
  border: 2px solid $baseColor;

  .search {
    width: 100%;
    height: 35px;

    input {
      width: 75%;
      height: 100%;
      padding-left: 5px;
      outline: none;
      border: 2px solid $baseColor;
      color: $baseColor;
      font-size: 1.2em;
      &::placeholder {
        color: $baseColor;
      }
      &:focus {
        border: 2px solid $accentColor;
      }
    }

    button {
      width: 100% - 75%;
      height: 100%;
      outline: none;
      border: none;
      background: $baseColor;
      color: white;
      font-size: 1.2em;
      &:hover {
        background: $accentColor;
        color: $baseColor;
      }
      &:active {
        background: $washColor;
        color: $accentColor;
      }
    }
  }

  .display-info {
    width: 100%;
    margin-top: 20px;

    .info-block {
      margin-top: 15px;

      span.accent {
        font-size: 1.6em;
        color: $accentColor;
      }
    }
  }
}
</style>
