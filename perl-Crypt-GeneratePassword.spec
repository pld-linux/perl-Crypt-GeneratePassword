#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Crypt
%define	pnam	GeneratePassword
Summary:	Crypt::GeneratePassword - generate secure random pronounceable passwords
Summary(pl):	Crypt::GeneratePassword - generuj bezpieczne, losowe, wymawialne has³a
Name:		perl-Crypt-GeneratePassword
Version:	0.02
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
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
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%{perl_sitelib}/%{pdir}/*.pm
%{perl_sitelib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
