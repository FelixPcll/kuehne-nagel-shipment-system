<template>
  <div class="list-item">
    <div class="container">
      <div class="track-ref prop head">Track code</div>
      <div class="from-coutry prop head">Country of dispatch</div>
      <div class="to-coutry prop head">Country of destination</div>
      <div class="package-weight prop head">Wgt. (kg)</div>
      <div class="options prop head">Options</div>
    </div>
    <ul class="list">
      <li class="row" v-for="(item) in shipments" :key="item.track_ref">
        <div class="track-ref prop body">
          <div class="text-info">{{ item.track_ref }}</div>
        </div>
        <div class="from-coutry prop body">
          <div v-if="item.is_up_to_date" class="text-info">{{ item.from_coutry }}</div>
          <input v-else type="text" class="text-edit" v-model="item.from_coutry" />
        </div>
        <div class="to-coutry prop body">
          <div v-if="item.is_up_to_date" class="text-info">{{ item.to_country }}</div>
          <input v-else type="text" class="text-edit" v-model="item.to_country" />
        </div>
        <div class="package-weight prop body">
          <div v-if="item.is_up_to_date" class="text-info">{{ item.package_weight }}</div>
          <input v-else type="number" class="text-edit" v-model="item.package_weight" />
        </div>
        <div class="options prop body">
          <div class="btn-holder">
            <button
              @click="updateBtn(item)"
              class="btn update"
            >{{ item.is_up_to_date?'Modify':'Save' }}</button>
            <button
              @click="deleteBtn(item)"
              class="btn delete"
            >{{ item.is_up_to_date?'Delete':'Cancel' }}</button>
          </div>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data: () => ({
    shipments: [],
  }),

  methods: {
    getShipments() {
      const apiUrl = 'http://localhost:8000/api/v0.1/shipment/';

      axios
        .get(apiUrl)
        .then((response) => {
          this.shipments = response.data;
        })
        .catch((e) => {
          console.log(e);
        });
    },

    updateBtn(item) {
      if (item.is_up_to_date) {
        if (this.shipments.some(shipment => !shipment.is_up_to_date)) {
          alert(
            "There's already one shipment modifying, please finish or cancel it first.",
          );
        } else {
          item.is_up_to_date = !item.is_up_to_date;
        }
      } else {
        item.track_ref = item.track_ref.toUpperCase();
        if (this.validateItem(item)) {
          this.updateShipment(item);
        }
      }
    },

    deleteBtn(item) {
      if (item.is_up_to_date) {
        this.deleteShipment(item);
      } else {
        this.getShipments();
      }
    },

    validateItem(item) {
      return true;
    },

    deleteShipment(item) {
      setTimeout(
        () => {
          if (
            confirm(
              `Press 'OK' if you're realy sure about deleting the shipment ${item.track_ref}`,
            )
          ) {
            const apiUrl = `http://localhost:8000/api/v0.1/shipment/${item.track_ref}`;

            axios
              .delete(apiUrl)
              .then((response) => {
                // console.log(response);
                this.getShipments();
                setTimeout(
                  () => {
                    alert(
                      `The shipment ${item.track_ref} was successfully deleted.`,
                    );
                  },
                  300,
                  item,
                );
              })
              .catch((e) => {
                console.log(e);
              });
          }
        },
        300,
        item,
      );
    },

    updateShipment(item) {
      if (confirm('Press "OK" to confirm the alterations on pakage.')) {
        // console.log("Hello from Post");
        item.is_up_to_date = !item.is_up_to_date;

        const apiUrl = `http://localhost:8000/api/v0.1/shipment/${item.track_ref}/`;

        axios
          .put(apiUrl, item)
          .then((response) => {
            console.log(response);
            this.getShipments();
          })
          .catch((e) => {
            alert(e);
            this.getShipments();
          });
      }
    },
  },

  created() {
    this.getShipments();
  },
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
    cursor: default;
  }
  .head {
    padding-bottom: 15px;
    font-size: $base-size;
    color: $accentColor;
  }

  li {
    border-top: 1px solid $baseColor;
  }

  .body {
    height: 32px;

    .text-info {
      padding-left: 4px;
      padding-top: 5px;
      padding-bottom: 5px;
    }
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

    .btn-holder {
      height: 100%;
      .btn {
        cursor: pointer;
        background: rgba($color: #000000, $alpha: 0);
        width: 53px;
        height: 24px;
        margin-right: 5px;
        margin-top: 3px;
        //margin-bottom: 4px;
        &:first-child {
          margin-left: 5px;
        }
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
}

.text-edit {
  width: calc(100% - 10px);
  height: 26px;
  margin-right: 5px;
  margin-top: 4px;
  padding-left: 3px;
  font-size: 16px;
  border: 1px solid $baseColor;
  background: rgba(0, 0, 0, 0);

  &:focus {
    border-color: $accentColor;
  }
}
</style>
