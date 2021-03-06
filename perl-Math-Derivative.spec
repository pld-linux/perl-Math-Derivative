%define		pdir	Math
%define		pnam	Derivative
Summary:	Math::Derivative perl module
Summary(pl.UTF-8):	Moduł perla Math::Derivative
Name:		perl-Math-Derivative
Version:	0.01
Release:	12
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a359b1b4b545c03f4147594fc64420a2
Patch0:		%{name}-man.patch
URL:		http://search.cpan.org/dist/Math-Derivative/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::Derivative - Numeric 1st and 2nd order differentiation.

%description -l pl.UTF-8
Moduł perla Math::Derivative - obliczający pochodne pierwszego i
drugiego rzędu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Math/Derivative.pm
%{_mandir}/man3/*
