import Ember from 'ember';

export default Ember.Controller.extend({
  datafiles: Ember.computed.mapBy('datasets', 'names'),
  classifier_files: Ember.computed.mapBy('classifiers', 'names'),
  fields: {},
  //selectedDatasets: [],
  //selectedClassifiers: [],
  selectedOutput: null,
  showPrecision: true,
  emptyDatasets: function() {
    var fields = this.get('fields');
    console.log(fields);
    var sel_datasets = fields.selectedDatasets;
    var sel_classifiers = fields.selectedClassifiers; //this.get('fields.selectedClassifiers');

    console.log("Empty datasets!");
    console.log(sel_datasets.length);
    console.log(sel_classifiers.length);

    return (sel_datasets.length === 0 || sel_classifiers.length === 0);
  }.property('fields', 'fields.selectedDatasets', 'fields.selectedClassifiers'),
  actions: {
    submit: function() {
      var fields = this.get('fields');
      var controller = this;
      console.log(fields);
      fields.classifier_ids = fields.selectedClassifiers;
      var selected_classifiers = fields.selectedClassifiers;
      //fields.classifiers = fields.selectedClassifiers;
      var analysis = this.store.createRecord('analysis', fields);


      var promiseArray = [];
      var dataset = this.store.find('dataset', fields.selectedDatasets);
      promiseArray.push(dataset);
      console.log(dataset);

      for(var i = 0; i < selected_classifiers.length; i++) {
        console.log("Classifier!");
        console.log(selected_classifiers[i]);
        var classifier = this.store.find('classifier', selected_classifiers[i]);
        promiseArray.push(classifier);
        console.log(classifier);
      }

      Promise.all(promiseArray).then(function(values) {
        console.log("Promise fulfilled!");
        console.log(values);
        console.log(values[1]);

        var classifiers_section = values.slice(1, values.length);
        analysis.set('dataset', values[0]);
        console.log(analysis.get('classifiers'));
        console.log(classifiers_section);
        analysis.get('classifiers').pushObjects(classifiers_section);
        console.log(analysis.get('classifiers'));
        console.log("Done! Now saving!");
        analysis.save().then(function(response) {
          console.log(response);
          controller.set('showMessage', true);
          controller.set('message', "Successfully created an analysis!");

          alert("Successfully created an analysis!");
        });
      });
  },

  toggleGraphs: function() {
    var value = this.get('showPrecision');
    this.set('showPrecision', !value);
  },

  selectOutput: function(output) {
    this.set('selectedOutput', output);
    console.log(output);
  }
 }
});