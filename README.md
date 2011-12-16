# Intro

vcardedit is a text-based editor for VCard files.

As of now it can perform the following actions:
- Fix names to be title cased
- Fix french phones (replacing 0[1-6] into +33[1-6], marking +336 phones as cellphones...)
- Interactively edit firstname and lastname

# Dependencies

vobject: http://vobject.skyhouseconsulting.com/

# License

GPL v3 or later

# Usage

    vcardedit <action> <in.vcf> <out.vcf>

Run it as `vcardedit --help` for more details.

# Author

Aurélien Gâteau <http://github.com/agateau>
