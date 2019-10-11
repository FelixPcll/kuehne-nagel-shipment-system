<template>
  <div class="list-item">
    <div class="container">
      <div class="track-ref prop head">Track Code</div>
      <div class="from-coutry prop head">Country of dispatch</div>
      <div class="to-coutry prop head">Country of destination</div>
      <div class="package-weight prop head">Wgt. (kg)</div>
      <div class="options prop head">Options</div>
    </div>
    <ul class="list">
      <li class="row" v-for="(item) in shipments" :key="item.track_ref">
        <div class="track-ref prop body">{{ item.track_ref }}</div>
        <div class="from-coutry prop body">{{ item.from_coutry }}</div>
        <div class="to-coutry prop body">{{ item.to_country }}</div>
        <div class="package-weight prop body">{{ item.package_weight }}</div>
        <div class="options prop body">
          <button @click="updateShipment(item)" class="btn update">Update</button>
          <button @click="deleteShipment(item)" class="btn delete">Delete</button>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data: () => {
    return {
      shipments: []
    };
  },

  methods: {
    getShipments() {
      let apiUrl = "http://localhost:8000/api/v0.1/shipment/";

      axios
        .get(apiUrl)
        .then(response => {
          this.shipments = response.data;
        })
        .catch(e => {
          console.log(e);
        });
    },

    deleteShipment(item) {
      setTimeout(
        () => {
          if (
            confirm(
              `Press 'OK' if you're realy sure about deleting the shipment ${item.track_ref}`
            )
          ) {
            let apiUrl = `http://localhost:8000/api/v0.1/shipment/${item.track_ref}`;

            axios
              .delete(apiUrl)
              .then(response => {
                this.getShipments();
                setTimeout(
                  () => {
                    alert(
                      `The shipment ${item.track_ref} was successfully deleted.`
                    );
                  },
                  300,
                  item
                );
              })
              .catch(e => {
                console.log(e);
              });
          }
        },
        300,
        item
      );
    },

    updateShipment(item) {
      console.log("Hello from Update");
    }
  },

  created() {
    this.getShipments();
  }
};
</script>

<style lang="scss" scoped>
@import "@/main.scss";

.list-item {
  //border: 2px solid $baseColor;
  padding: 10px;

  .row {
    &:hover {
      background: $washColor;
    }
  }

  .prop {
    display: inline-block;
    padding-left: 4px;
  }
  .head {
    padding-bottom: 15px;
    font-size: $base-size;
    color: $accentColor;
  }
  .body {
    border-top: 1px solid $baseColor;
    padding-top: 5px;
    padding-bottom: 5px;
    height: 32px;
  }
}

.list-item {
  .track-ref {
    width: 15%;
  }
  .from-coutry {
    width: 32%;
  }
  .to-coutry {
    width: 32%;
  }
  .package-weight {
    width: 9%;
  }
  .options {
    width: 12%;
    padding-left: 0;

    .btn {
      cursor: pointer;
      background: rgba($color: #000000, $alpha: 0);
      border: none;
      height: 99%;
      width: 53px;
      margin-right: 5px;
      &:last-child {
        margin-right: 0;
      }

      &.delete {
        border: 1px solid $alertColor;
        color: $alertColor;

        &:hover {
          border: none;
          background: $alertColor;
          color: $washColor;
        }
        &:active {
          background: $washColor;
          color: $alertColor;
        }
      }
      &.update {
        border: 1px solid $baseColor;
        color: $baseColor;
        &:hover {
          border: none;
          background: $baseColor;
          color: $washColor;
        }
        &:active {
          background: $washColor;
          color: $baseColor;
        }
      }
    }
  }
}
</style>
