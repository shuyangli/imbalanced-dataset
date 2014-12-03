import Ember from 'ember';

export default Ember.Route.extend({
  model: function() {

  },

  setupController: function(controller, model) {
     this._super(controller,model);
     controller.set('datasets', this.store.find('dataset'));
     controller.set('classifiers', this.store.find('classifier'));
  }
});
