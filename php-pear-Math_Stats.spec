%include	/usr/lib/rpm/macros.php
%define		_class		Math
%define		_subclass	Stats
%define		_status		beta

%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - Classes to calculate statistical parameters
Summary(pl):	%{_class}_%{_subclass} - klasy do obliczania parametrów statystycznych
Name:		php-pear-%{_pearname}
Version:	0.9.0
Release:	0.beta3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}beta3.tgz
# Source0-md5:	ffc0b653e5e2985113262a5299ebe69b
URL:		http://pear.php.net/package/%{_pearname}/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Classes to calculate statistical parameters of numerical arrays of
data. The data can be in a simple numerical array, or in a cummulative
numerical array. A cummulative array, has the value as the index and
the number of repeats as the value for the array item, e.g. $data =
array(3=>4, 2.3=>5, 1.25=>6, 0.5=>3). Nulls can be rejected, ignored
or handled as zero values.

This class has in PEAR status: %{_status}.

%description -l pl
Ten pakiet zawiera klasy s³u¿±ce do obliczania parametrów
statystycznych z tablic danych. Dane mog± byæ w zwyk³ej tablicy
numerycznej lub w tablicy skumulowanej. Tablica skumulowana zawiera
indeksy i liczby wyst±pieñ warto¶ci dla elementu tablicy, np. $data =
array(3=>4, 2.3=>5, 1.25=>6, 0.5=>3). Puste elementy mog± byæ
odrzucone, ignorowane lub taktowane jako warto¶ci zerowe.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}beta3/*.php	$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}beta3/{examples/*,README*}
%{php_pear_dir}/%{_class}/*.php
