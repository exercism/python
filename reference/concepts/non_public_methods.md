# Non public methods

TODO: ADD MORE

- Methods or attributes (including those of an imported module) prefixed with an underscore, `_`, are conventionally treated as "non-public" methods. Python does not support data privacy in the way a language like Java does. Instead convention dictates that methods and attributes that are not prefixed with a single underscore can be expected to remain stable along with semver, i.e. a public method will be backwards compatible with minor version updates, and can change with major version updates. Generally, importing non-public functions or using non-public methods is discouraged, though Python will not explicitly stop the programmer from doing so. [phone-number](../exercise-concepts/phone-number.md)
