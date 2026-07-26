%define upstream_name    Catalyst-Plugin-Captcha
Name:		perl-%{upstream_name}
Version:	0.04
Release:	7

Summary:	Create and validate Captcha for Catalyst
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Catalyst-Plugin-Captcha
Source0:	https://cpan.metacpan.org/authors/id/D/DI/DIEGOK/Catalyst-Plugin-Captcha-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst)
BuildRequires:	perl(Catalyst::Plugin::Session)
BuildRequires:	perl(GD::SecurityImage)
BuildRequires:	perl(HTTP::Date)
BuildArch:	noarch

%description
This plugin create, validate Captcha.

Note: This plugin uses GD::SecurityImage and requires a session
plugins like Catalyst::Plugin::Session

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.40.0-2mdv2011.0
+ Revision: 654258
- rebuild for updated spec-helper

* Mon Oct 11 2010 Buchan Milne <bgmilne@mandriva.org> 0.40.0-1mdv2011.0
+ Revision: 584945
- import perl-Catalyst-Plugin-Captcha

