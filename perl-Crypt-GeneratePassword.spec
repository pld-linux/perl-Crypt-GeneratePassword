#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Crypt
%define	pnam	GeneratePassword
Summary:	Crypt::GeneratePassword - generate secure random pronounceable passwords
Summary(pl):	Crypt::GeneratePassword - generuj bezpieczne, losowe, wymawialne has³a
Name:		perl-Crypt-GeneratePassword
Version:	0.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	65a9e924ba7496ebd13b70d863d8ae1b
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::GeneratePassword generates random passwords that are (more or less)
pronounceable.  Unlike Crypt::RandPasswd, it doesn't use the FIPS-181
NIST standard, which is proven to be insecure.  It does use a similar
interface, so it should be a drop-in replacement in most cases.

%description -l pl
Crypt::GeneratePassword generuje losowe has³a, (lepiej lub gorzej)
wymawialne.  W odró¿nieniu od Crypt::RandPasswd, nie u¿ywa on standardu
FIPS-181 NIST, który -- jak udowodniono -- nie jest bezpieczny.  U¿ywa za
to podobnego interfejsu, wiêc zastêpowanie w wiêkszo¶ci przypadków
powinno byæ bezproblemowe.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
