Summary:	Source code completion library
Summary(pl.UTF-8):	Biblioteka dopełniania dla kodu źródłowego
Name:		gtksourcecompletion
Version:	0.5.2
Release:	1
License:	LGPL v2+
Group:		Applications
Source0:	http://dl.sourceforge.net/gtksourcecomple/%{name}-%{version}.tar.gz
# Source0-md5:	b031896ce03bef4ca711f9b1e0a34544
URL:		http://gtksourcecomple.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gedit2-devel
BuildRequires:	glib2-devel >= 1:2.12.0
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Source code completion library.

%description -l pl.UTF-8
Biblioteka dopełniania dla kodu źródłowego.

%package devel
Summary:	Header files for gtksourcecompletion library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gtksourcecompletion
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for gtksourcecompletion library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gtksourcecompletion.

%package static
Summary:	Static gtksourcecompletion library
Summary(pl.UTF-8):	Statyczna biblioteka gtksourcecompletion
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gtksourcecompletion library.

%description static -l pl.UTF-8
Statyczna biblioteka gtksourcecompletion.

%package apidocs
Summary:	gtksourcecompletion API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki gtksourcecompletion
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
gtksourcecompletion API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki gtksourcecompletion.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO NEWS TODO
%attr(755,root,root) %{_libdir}/libgtksourcecompletion-1.0.so.1.0.0
%attr(755,root,root) %ghost %{_libdir}/libgtksourcecompletion-1.0.so.1
%{_datadir}/gtksourcecompletion

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtksourcecompletion-1.0.so
%{_libdir}/libgtksourcecompletion-1.0.la
%{_includedir}/gtksourcecompletion-1.0
%{_pkgconfigdir}/gtksourcecompletion-1.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgtksourcecompletion-1.0.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gtksourcecompletion-1.0
