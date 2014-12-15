import Ember from 'ember';

export default Ember.Route.extend({
  model: function() {
    var model = this.store.createRecord('dataset');
    return model;
  },
  setupController: function(controller, model) {
    //this._super(controller,model);
    controller.set('fields', {});
    controller.set("model", model);
  }
});
