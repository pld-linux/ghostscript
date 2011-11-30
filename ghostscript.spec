# TODO:
# - fix svga bcond
# - add djvu driver:
#   http://dl.sourceforge.net/djvu/gsdjvu-1.3.tar.gz (or newer)
#
# Conditional build:
%bcond_without	cairo		# disable cairo support (for cairo bootstrap)
%bcond_without	system_jbig2dec	# build with included jbig2dec
%bcond_with	svga		# svgalib display support (vgalib,lvga256 devices) [broken in sources]
%bcond_without	gtk		# gsx (GTK+ based frontend)

Summary:	PostScript & PDF interpreter and renderer
Summary(de.UTF-8):	PostScript & PDF Interpreter und Renderer
Summary(fr.UTF-8):	Interpréteur et visualisateur PostScript & PDF
Summary(ja.UTF-8):	PostScript インタープリタ・レンダラー
Summary(pl.UTF-8):	Bezpłatny interpreter i renderer PostScriptu i PDF
Summary(tr.UTF-8):	PostScript & PDF yorumlayıcı ve gösterici
Name:		ghostscript
Version:	9.04
Release:	2
License:	GPL v3+
Group:		Applications/Graphics
Source0:	http://downloads.sourceforge.net/ghostscript/%{name}-%{version}.tar.bz2
# Source0-md5:	9f6899e821ab6d78ab2c856f10fa3023
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	9b5953aa0cc155f4364f20036b848585
Patch0:		%{name}-missquotes.patch
Patch1:		%{name}-setuid.patch
Patch2:		%{name}-time_h.patch
Patch5:		%{name}-cups-sh.patch
Patch6:		%{name}-gdevcd8-fixes.patch
Patch7:		%{name}-fPIC.patch
Patch8:		%{name}-zlib.patch
Patch9:		%{name}-git.patch

# fedora
Patch20: ghostscript-scripts.patch
Patch21: ghostscript-runlibfileifexists.patch
Patch22: ghostscript-cups-rgbw.patch
Patch23: ghostscript-glyph-crash.patch
Patch24: ghostscript-jbig2dec-nullderef.patch
Patch25: ghostscript-SEAC.patch
Patch26: ghostscript-cups-filters.patch
Patch27: ghostscript-Fontmap.local.patch
Patch28: ghostscript-iccprofiles-initdir.patch
Patch29: ghostscript-gdevcups-debug-uninit.patch
Patch30: ghostscript-pxl-landscape.patch

URL:		http://www.ghostscript.com/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1.6
%{?with_cairo:BuildRequires:	cairo-devel >= 1.2.0}
BuildRequires:	cups-devel
BuildRequires:	dbus-devel
BuildRequires:	docbook-style-dsssl
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2.0
%{?with_gtk:BuildRequires:	gtk+2-devel >= 1:2.0.0}
%{?with_system_jbig2dec:BuildRequires:	jbig2dec-devel}
BuildRequires:	libidn-devel
BuildRequires:	libpaper-devel
BuildRequires:	libpng-devel >= 1.2.42
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel >= 3.9.2
BuildRequires:	libtool
BuildRequires:	pkgconfig
# Required by 'gdevvglb' device.
%{?with_svga:BuildRequires:	svgalib-devel}
BuildRequires:	tar >= 1:1.22
# for documentation regeneration
BuildRequires:	tetex
BuildRequires:	tetex-dvips
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	zlib-devel >= 1.2.3
Obsoletes:	ghostscript-afpl
Obsoletes:	ghostscript-esp
Obsoletes:	ghostscript-gpl
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

%package cups
Summary:	Ghostscript CUPS files
Summary(pl.UTF-8):	Pliki Ghostscripta dla CUPS-a
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description cups
This package contains CUPS files provided by ghostscript.

%description cups -l pl.UTF-8
Ten pakiet zawiera pliki dla CUPS-a dostarczane przez ghostscript.

%package gtk
Summary:	Ghostscript with GTK+ console
Summary(pl.UTF-8):	Ghostscript z konsolą GTK+
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}
Obsoletes:	ghostscript-afpl-gtk
Obsoletes:	ghostscript-esp-gtk
Obsoletes:	ghostscript-gpl-gtk

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
Obsoletes:	ghostscript-afpl-devel
Obsoletes:	ghostscript-esp-devel

%description devel
Header files for libgs - ghostscript shared library.

%description devel -l pl.UTF-8
Pliki nagłówkowe libgs - współdzielonej biblioteki ghostscript.

%package ijs-devel
Summary:	IJS development files
Summary(pl.UTF-8):	Pliki dla programistów IJS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	ghostscript-afpl-ijs-devel
Obsoletes:	ghostscript-esp-ijs-devel

%description ijs-devel
IJS development files.

%description ijs-devel -l pl.UTF-8
Pliki do tworzenia programów z użyciem biblioteki IJS.

%package ijs-static
Summary:	Static libijs library
Summary(pl.UTF-8):	Statyczna biblioteka IJS
Group:		Development/Libraries
Requires:	%{name}-ijs-devel = %{version}-%{release}
Obsoletes:	ghostscript-afpl-ijs-static
Obsoletes:	ghostscript-esp-ijs-static

%description ijs-static
Static libijs library.

%description ijs-static -l pl.UTF-8
Statyczna wersja biblioteki IJS.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p2

%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1

%build
%if %{with system_jbig2dec}
%{__rm} -r jbig2dec
%endif
# use system libs (sources contain unmodified zlib 1.2.3 and libpng 1.2.42)
%{__rm} -r libpng zlib
# jpeg is built with different configuration (D_MAX_BLOCKS_IN_MCU=64), jasper and lcms are modified
cd jasper
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
cd ..
%{__aclocal}
%{__autoconf}
%configure \
	CFLAGS="%{rpmcflags} -DA4" \
	%{!?with_cairo:--disable-cairo} \
	--disable-compile-inits \
	--enable-dynamic \
	--with-drivers=ALL%{?with_svga:,vgalib,lvga256} \
	--with-fontpath="%{_datadir}/fonts:%{_datadir}/fonts/Type1" \
	--with-ijs \
	--with-install-cups \
	--with-jbig2dec \
	--with-jasper \
	--with-pdftoraster \
	--with-system-libtiff \
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

%{__rm} $RPM_BUILD_ROOT%{_bindir}/*.sh \
	$RPM_BUILD_ROOT%{_mandir}/man1/{ps2pdf1{2,3},eps2eps}.1 \
	$RPM_BUILD_ROOT%{_mandir}/de/man1/{ps2pdf1{2,3},eps2eps}.1

echo ".so gs.1"     > $RPM_BUILD_ROOT%{_mandir}/man1/ghostscript.1
echo ".so ps2pdf.1" > $RPM_BUILD_ROOT%{_mandir}/man1/ps2pdf12.1
echo ".so ps2pdf.1" > $RPM_BUILD_ROOT%{_mandir}/man1/ps2pdf13.1
echo ".so ps2ps.1"  > $RPM_BUILD_ROOT%{_mandir}/man1/eps2eps.1
echo ".so gslp.1"   > $RPM_BUILD_ROOT%{_mandir}/man1/gsbj.1
echo ".so gslp.1"   > $RPM_BUILD_ROOT%{_mandir}/man1/gsdj.1
echo ".so gslp.1"   > $RPM_BUILD_ROOT%{_mandir}/man1/gsdj500.1
echo ".so gslp.1"   > $RPM_BUILD_ROOT%{_mandir}/man1/gslj.1

echo ".so ps2ps.1"  > $RPM_BUILD_ROOT%{_mandir}/de/man1/eps2eps.1
echo ".so ps2pdf.1" > $RPM_BUILD_ROOT%{_mandir}/de/man1/ps2pdf12.1
echo ".so ps2pdf.1" > $RPM_BUILD_ROOT%{_mandir}/de/man1/ps2pdf13.1

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

#mv -f $RPM_BUILD_ROOT%{_bindir}/{gsc,gs}
ln -sf gs $RPM_BUILD_ROOT%{_bindir}/gsc
ln -sf gs $RPM_BUILD_ROOT%{_bindir}/ghostscript
ln -s gstoraster $RPM_BUILD_ROOT%{_ulibdir}/cups/filter/pdftoraster
ln -s gstoraster $RPM_BUILD_ROOT%{_ulibdir}/cups/filter/pstoraster

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}
%attr(755,root,root) %{_bindir}/dumphint
%attr(755,root,root) %{_bindir}/dvipdf
%attr(755,root,root) %{_bindir}/eps2eps
%attr(755,root,root) %{_bindir}/font2c
%attr(755,root,root) %{_bindir}/ghostscript
%attr(755,root,root) %{_bindir}/gs
%attr(755,root,root) %{_bindir}/gsbj
%attr(755,root,root) %{_bindir}/gsc
%attr(755,root,root) %{_bindir}/gsdj
%attr(755,root,root) %{_bindir}/gsdj500
%attr(755,root,root) %{_bindir}/gslj
%attr(755,root,root) %{_bindir}/gslp
%attr(755,root,root) %{_bindir}/gsnd
%attr(755,root,root) %{_bindir}/ijs_client_example
%attr(755,root,root) %{_bindir}/ijs_server_example
%attr(755,root,root) %{_bindir}/pdf2dsc
%attr(755,root,root) %{_bindir}/pdf2ps
%attr(755,root,root) %{_bindir}/pdfopt
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
%attr(755,root,root) %{_bindir}/wftopfa
%attr(755,root,root) %{_libdir}/libgs.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libgs.so.9
%attr(755,root,root) %{_libdir}/libijs-*.so
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/%{version}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/%{version}
%{_datadir}/%{name}/%{version}/Resource
%{_datadir}/%{name}/%{version}/iccprofiles
%dir %{_datadir}/%{name}/%{version}/lib
%{_datadir}/%{name}/%{version}/examples
%{_datadir}/%{name}/%{version}/lib/*.ppd
%{_datadir}/%{name}/%{version}/lib/*.ps
%{_datadir}/%{name}/%{version}/lib/*.rpd
%{_datadir}/%{name}/%{version}/lib/*.src
%{_datadir}/%{name}/%{version}/lib/*.upp
%{_datadir}/%{name}/%{version}/lib/*.x[bp]m
%{_mandir}/man1/dvipdf.1*
%{_mandir}/man1/eps2eps.1*
%{_mandir}/man1/font2c.1*
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
%{_mandir}/man1/pdfopt.1*
%{_mandir}/man1/pf2afm.1*
%{_mandir}/man1/pfbtopfa.1*
%{_mandir}/man1/printafm.1*
%{_mandir}/man1/ps2ascii.1*
%{_mandir}/man1/ps2epsi.1*
%{_mandir}/man1/ps2pdf.1*
%{_mandir}/man1/ps2pdf12.1*
%{_mandir}/man1/ps2pdf13.1*
%{_mandir}/man1/ps2pdfwr.1*
%{_mandir}/man1/ps2ps.1*
%{_mandir}/man1/wftopfa.1*
%lang(cs) %{_mandir}/cs/man1/*
%lang(de) %{_mandir}/de/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(pl) %{_mandir}/pl/man1/*

%files cups
%defattr(644,root,root,755)
%attr(755,root,root) %{_ulibdir}/cups/filter/gstoraster
%attr(755,root,root) %{_ulibdir}/cups/filter/pdftoraster
%attr(755,root,root) %{_ulibdir}/cups/filter/pstoraster
%attr(755,root,root) %{_ulibdir}/cups/filter/pstopxl
%{_datadir}/cups/model/pxlcolor.ppd
%{_datadir}/cups/model/pxlmono.ppd
%{_datadir}/cups/mime/gstoraster.convs

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

%files ijs-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ijs-config
%attr(755,root,root) %{_libdir}/libijs.so
%{_libdir}/libijs.la
%{_includedir}/ijs
%{_pkgconfigdir}/ijs.pc
%{_mandir}/man1/ijs-config.1*

%files ijs-static
%defattr(644,root,root,755)
%{_libdir}/libijs.a
