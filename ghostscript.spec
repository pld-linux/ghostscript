# TODO:
# - add djvu driver:
#   http://dl.sourceforge.net/djvu/gsdjvu-1.3.tar.gz (or newer)
#
# Conditional build:
%bcond_without	cairo		# cairo support (disable for cairo bootstrap)
%bcond_without	system_freetype	# system freetype
%bcond_without	system_jbig2dec	# system jbig2dec
%bcond_with	system_libjpeg	# system libjpeg (incompatible with D_MAX_BLOCKS_IN_MCU=64 variant)
%bcond_with	system_libtiff	# system libtiff (incompatible with modified libjpeg)
%bcond_without	system_openjp2	# system openjpeg2
%bcond_with	system_lcms2	# build with included lcms2 (which is thread safe)
%bcond_without	gtk		# gsx (GTK+ based frontend)
%bcond_without	texdocs		# skip tetex BRs

Summary:	PostScript & PDF interpreter and renderer
Summary(de.UTF-8):	PostScript & PDF Interpreter und Renderer
Summary(fr.UTF-8):	Interpréteur et visualisateur PostScript & PDF
Summary(ja.UTF-8):	PostScript インタープリタ・レンダラー
Summary(pl.UTF-8):	Bezpłatny interpreter i renderer PostScriptu i PDF
Summary(tr.UTF-8):	PostScript & PDF yorumlayıcı ve gösterici
Name:		ghostscript
Version:	10.02.0
Release:	1
License:	AGPL v3+
Group:		Applications/Graphics
#Source0Download: https://github.com/ArtifexSoftware/ghostpdl-downloads/releases
Source0:	https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs10020/%{name}-%{version}.tar.xz
# Source0-md5:	80c1cdfada72f2eb5987dc0d590ea5b2
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	9b5953aa0cc155f4364f20036b848585
Patch0:		%{name}-missquotes.patch
Patch1:		%{name}-a4.patch
Patch2:		ijs-pkgconfig.patch

Patch6:		%{name}-gdevcd8-fixes.patch

# fedora
Patch20:	%{name}-scripts.patch

Patch28:	%{name}-iccprofiles-initdir.patch

URL:		http://www.ghostscript.com/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1.6
%{?with_cairo:BuildRequires:	cairo-devel >= 1.2.0}
BuildRequires:	cups-devel >= 1.5
BuildRequires:	dbus-devel
BuildRequires:	docbook-style-dsssl
BuildRequires:	fontconfig-devel
%{?with_system_freetype:BuildRequires:	freetype-devel >= 1:2.10.4}
%{?with_gtk:BuildRequires:	gtk+3-devel >= 3.0}
%{?with_system_jbig2dec:BuildRequires:	jbig2dec-devel >= 0.19}
%{?with_system_lcms2:BuildRequires:	lcms2-devel >= 2.6}
BuildRequires:	libidn-devel
%{?with_system_libjpeg:BuildRequires:	libjpeg-devel >= 9c}
BuildRequires:	libpaper-devel
BuildRequires:	libpng-devel >= 2:1.6.37
BuildRequires:	libstdc++-devel
%{?with_system_libtiff:BuildRequires:	libtiff-devel >= 4.2.0}
BuildRequires:	libtool
%{?with_system_openjp2:BuildRequires:	openjpeg2-devel}
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	tar >= 1:1.22
# for documentation regeneration
%if %{with texdocs}
BuildRequires:	tetex
BuildRequires:	tetex-dvips
%endif
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xz
BuildRequires:	zlib-devel >= 1.2.11
%{?with_system_freetype:Requires:	freetype >= 1:2.10.4}
%{?with_system_jbig2dec:Requires:	jbig2dec >= 0.19}
%{?with_system_lcms2:Requires:	lcms2 >= 2.6}
%{?with_system_libjpeg:Requires:	libjpeg >= 9c}
Requires:	libpng >= 2:1.6.37
%{?with_system_libtiff:Requires:	libtiff >= 4.2.0}
Requires:	zlib >= 1.2.11
Obsoletes:	ghostscript-afpl < 8.54
Obsoletes:	ghostscript-esp < 8.50
Obsoletes:	ghostscript-gpl < 8.51
Obsoletes:	ghostscript-svga < 9.24
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ulibdir        %{_prefix}/lib

%description
cos nGhostscript is a PostScript interpreter. It can render both
PostScript and PDF compliant files to devices which include an X
window, many printer formats (including support for color printers),
and popular graphics file formats.

%description -l de.UTF-8
Ghostscipt ist ein PostScript-Interpretierer. Er kann sowohl
PostScript als auch PDF-konforme Dateien an Geräte ausgeben, zu denen
ein X-Fenster, viele Druckerformate (einschließlich Support für
Farbdrucker) und gängige Grafikdateiformate zählen.

%description -l fr.UTF-8
Ghostscript est un interpréteur PostScript. Il peut rendre des
fichiers PostScript ou PDF sur des périphériques dont une fenêtre X,de
nombreux types d'imprimantes (dont un support pour imprimantes
couleur), et des formats de fichiers graphiques populaires.

%description -l ja.UTF-8
Ghostscript は PostScript インタープリタです。ポストスクリプトと PDF をレンダリングし、X window
や他のプリンタフォーマットで出力 します。このパッケージは日本語対応しています。

%description -l pl.UTF-8
Ghostcript jest interpreterem PostScriptu, języka używanego do opisu
formatu dokumentu. Ghostscript potrafi przetworzyć dokument w formacie
PostScript i PDF na szereg postaci wyjściowych: drukarki (włączając
kolorowe), okno X-Window i popularne formaty graficzne.

%description -l tr.UTF-8
GhostScript, PostScript ve PDF uyumlu dosyaları, X penceresinde
gösterebilir ve birçok yazıcının (renkli yazıcılar dahil) basabileceği
biçime getirebilir.

%package gtk
Summary:	Ghostscript with GTK+ console
Summary(pl.UTF-8):	Ghostscript z konsolą GTK+
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}
Obsoletes:	ghostscript-afpl-gtk < 8.54
Obsoletes:	ghostscript-esp-gtk < 8.50
Obsoletes:	ghostscript-gpl-gtk < 8.51

%description gtk
Ghostscript with GTK+ console.

%description gtk -l pl.UTF-8
Ghostscript z konsolą GTK+.

%package x11
Summary:	X Window System drivers for Ghostscript
Summary(pl.UTF-8):	Sterowniki systemu X Window dla Ghostscripta
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description x11
X Window System output drivers for Ghostscript: x11, x11alpha.

%description x11 -l pl.UTF-8
Sterowniki wyjściowe systemu X Window dla Ghostscripta: x11, x11alpha.

%package devel
Summary:	libgs header files
Summary(pl.UTF-8):	Pliki nagłówkowe libgs
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	ghostscript-afpl-devel < 8.54
Obsoletes:	ghostscript-esp-devel < 8.50

%description devel
Header files for libgs - ghostscript shared library.

%description devel -l pl.UTF-8
Pliki nagłówkowe libgs - współdzielonej biblioteki ghostscript.

%package doc
Summary:	Documentation for ghostscript
Group:		Documentation
BuildArch:	noarch

%description doc
The documentation files that come with ghostscript.

%package ijs
Summary:	IJS (InkJet Server) shared library
Summary(pl.UTF-8):	Biblioteka współdzielona IJS (InkJet Server)
Group:		Libraries
Conflicts:	ghostscript < 9.10-2

%description ijs
IJS (InkJet Server) Raster Image Transport Protocol shared library.

%description ijs -l pl.UTF-8
Biblioteka współdzielona protokołu transportu obrazów rastrowych IJS
(InkJet Server).

%package ijs-devel
Summary:	IJS development files
Summary(pl.UTF-8):	Pliki dla programistów IJS
Group:		Development/Libraries
Requires:	%{name}-ijs = %{version}-%{release}
Obsoletes:	ghostscript-afpl-ijs-devel < 8.54
Obsoletes:	ghostscript-esp-ijs-devel < 8.50

%description ijs-devel
IJS development files.

%description ijs-devel -l pl.UTF-8
Pliki do tworzenia programów z użyciem biblioteki IJS.

%package ijs-static
Summary:	Static libijs library
Summary(pl.UTF-8):	Statyczna biblioteka IJS
Group:		Development/Libraries
Requires:	%{name}-ijs-devel = %{version}-%{release}
Obsoletes:	ghostscript-afpl-ijs-static < 8.54
Obsoletes:	ghostscript-esp-ijs-static < 8.50

%description ijs-static
Static libijs library.

%description ijs-static -l pl.UTF-8
Statyczna wersja biblioteki IJS.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%patch6 -p1

%patch20 -p1

%patch28 -p1

# use system libs:
# freetype 2.10.4
%{?with_system_freetype:%{__rm} -r freetype}
# jbig2dec 0.19
%{?with_system_jbig2dec:%{__rm} -r jbig2dec}
# (unmodified) libpng 1.6.37 and zlib 1.2.11
%{__rm} -r libpng zlib
# libjpeg (9d with additional CLAMP_DC) is built with different configuration (D_MAX_BLOCKS_IN_MCU=64)
%{?with_system_libjpeg:%{__rm} -r jpeg}
# lcms2mt is thread safe version of lcms2 2.10
%{?with_system_lcms2:%{__rm} -r lcms2mt}
# leptonica 1.81.0-git (for tesseract), no switch to use system
# openjpeg 2.4.0
%{?with_system_openjp2:%{__rm} -r openjpeg}
# tesseract 5.0.0-alpha, no switch to use system

%build
%{__aclocal}
%{__autoconf}
%configure \
	%{!?with_cairo:--disable-cairo} \
	--disable-compile-inits \
        --enable-dynamic --disable-hidden-visibility \
	--with-drivers=ALL \
	--with-fontpath="%{_datadir}/fonts:%{_datadir}/fonts/Type1" \
	--with-ijs \
	--with-jbig2dec \
	--with-pdftoraster \
	%{?with_system_libtiff:--with-system-libtiff} \
	--with-x

cd ijs
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-shared
%{__make}
cd ..

%{__make} -j1 so \
	docdir=%{_docdir}/%{name}-%{version}

%{__make} -j1 \
	docdir=%{_docdir}/%{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} soinstall \
	DESTDIR=$RPM_BUILD_ROOT \
	docdir=%{_docdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	docdir=%{_docdir}/%{name}-%{version}

%{__make} -C ijs install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p base/gserrors.h $RPM_BUILD_ROOT%{_includedir}/ghostscript

cp -p LICENSE $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%{__rm} $RPM_BUILD_ROOT%{_bindir}/*.sh \
	$RPM_BUILD_ROOT%{_mandir}/man1/{ps2pdf1{2,3},eps2eps}.1

echo ".so gs.1"     > $RPM_BUILD_ROOT%{_mandir}/man1/ghostscript.1
echo ".so ps2pdf.1" > $RPM_BUILD_ROOT%{_mandir}/man1/ps2pdf12.1
echo ".so ps2pdf.1" > $RPM_BUILD_ROOT%{_mandir}/man1/ps2pdf13.1
echo ".so ps2ps.1"  > $RPM_BUILD_ROOT%{_mandir}/man1/eps2eps.1
echo ".so gslp.1"   > $RPM_BUILD_ROOT%{_mandir}/man1/gsbj.1
echo ".so gslp.1"   > $RPM_BUILD_ROOT%{_mandir}/man1/gsdj.1
echo ".so gslp.1"   > $RPM_BUILD_ROOT%{_mandir}/man1/gsdj500.1
echo ".so gslp.1"   > $RPM_BUILD_ROOT%{_mandir}/man1/gslj.1

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
%{__rm} $RPM_BUILD_ROOT%{_mandir}/README.ghostscript-non-english-man-pages

ln -sf gs $RPM_BUILD_ROOT%{_bindir}/gsc
ln -sf gs $RPM_BUILD_ROOT%{_bindir}/ghostscript

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	ijs -p /sbin/ldconfig
%postun	ijs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dvipdf
%attr(755,root,root) %{_bindir}/eps2eps
%attr(755,root,root) %{_bindir}/ghostscript
%attr(755,root,root) %{_bindir}/gs
%attr(755,root,root) %{_bindir}/gsbj
%attr(755,root,root) %{_bindir}/gsc
%attr(755,root,root) %{_bindir}/gsdj
%attr(755,root,root) %{_bindir}/gsdj500
%attr(755,root,root) %{_bindir}/gslj
%attr(755,root,root) %{_bindir}/gslp
%attr(755,root,root) %{_bindir}/gsnd
%attr(755,root,root) %{_bindir}/pdf2dsc
%attr(755,root,root) %{_bindir}/pdf2ps
%attr(755,root,root) %{_bindir}/pf2afm
%attr(755,root,root) %{_bindir}/pfbtopfa
%attr(755,root,root) %{_bindir}/printafm
%attr(755,root,root) %{_bindir}/ps2ascii
%attr(755,root,root) %{_bindir}/ps2epsi
%attr(755,root,root) %{_bindir}/ps2pdf
%attr(755,root,root) %{_bindir}/ps2pdf12
%attr(755,root,root) %{_bindir}/ps2pdf13
%attr(755,root,root) %{_bindir}/ps2pdf14
%attr(755,root,root) %{_bindir}/ps2pdfwr
%attr(755,root,root) %{_bindir}/ps2ps
%attr(755,root,root) %{_bindir}/ps2ps2
%attr(755,root,root) %{_bindir}/pphs
%attr(755,root,root) %{_libdir}/libgs.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libgs.so.10
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/%{version}
%{_datadir}/%{name}/%{version}/Resource
%{_datadir}/%{name}/%{version}/iccprofiles
%dir %{_datadir}/%{name}/%{version}/lib
%{_datadir}/%{name}/%{version}/lib/*.ppd
%{_datadir}/%{name}/%{version}/lib/*.ps
%{_datadir}/%{name}/%{version}/lib/*.rpd
%{_datadir}/%{name}/%{version}/lib/*.upp
%{_datadir}/%{name}/%{version}/lib/*.x[bp]m
%{_mandir}/man1/dvipdf.1*
%{_mandir}/man1/eps2eps.1*
%{_mandir}/man1/ghostscript.1*
%{_mandir}/man1/gs.1*
%{_mandir}/man1/gsbj.1*
%{_mandir}/man1/gsdj.1*
%{_mandir}/man1/gsdj500.1*
%{_mandir}/man1/gslj.1*
%{_mandir}/man1/gslp.1*
%{_mandir}/man1/gsnd.1*
%{_mandir}/man1/pdf2dsc.1*
%{_mandir}/man1/pdf2ps.1*
%{_mandir}/man1/pf2afm.1*
%{_mandir}/man1/pfbtopfa.1*
%{_mandir}/man1/printafm.1*
%{_mandir}/man1/ps2ascii.1*
%{_mandir}/man1/ps2epsi.1*
%{_mandir}/man1/ps2pdf.1*
%{_mandir}/man1/ps2pdf12.1*
%{_mandir}/man1/ps2pdf13.1*
%{_mandir}/man1/ps2pdf14.1*
%{_mandir}/man1/ps2pdfwr.1*
%{_mandir}/man1/ps2ps.1*
%lang(cs) %{_mandir}/cs/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(pl) %{_mandir}/pl/man1/*

%files doc
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}

%if %{with gtk}
%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gsx
%endif

%files x11
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/%{version}/X11.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgs.so
%{_includedir}/ghostscript

%files ijs
%defattr(644,root,root,755)
%doc ijs/README
%attr(755,root,root) %{_bindir}/ijs_client_example
%attr(755,root,root) %{_bindir}/ijs_server_example
%attr(755,root,root) %{_libdir}/libijs-*.so

%files ijs-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libijs.so
%{_libdir}/libijs.la
%{_includedir}/ijs
%{_pkgconfigdir}/ijs.pc

%files ijs-static
%defattr(644,root,root,755)
%{_libdir}/libijs.a
