Changes
=======

tip (unreleased)
----------------

- Added get_full_names() which mimics get_full_name(), but takes an optional
  `count` argument. This new function caches the name files and attempts to
  make use of all system cores to generate names a little quicker.
- get_name() adjusted to check for the presence of a cache before manually
  reading from a file.
- Modified names.get_first_name to only accept 'male' and 'female' gender values

0.3.0 (2013-05-14)
------------------

- Fixed Python 3 support
- Improved tests and fixed minor bugs


0.2 (2013-02-17)
----------------

- Initial release
