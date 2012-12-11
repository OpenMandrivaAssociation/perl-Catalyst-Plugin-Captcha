%define upstream_name    Catalyst-Plugin-Captcha
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Create and validate Captcha for Catalyst
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

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
%setup -q -n %{upstream_name}-%{upstream_version}

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

