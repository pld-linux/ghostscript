#
# TODO:
#	- fix svga bcond
#
# Conditional build:
%bcond_without	system_jbig2dec	# build with included jbig2dec
%bcond_with	svga		# with svgalib display support (vgalib and lvga256 devices)
%bcond_without	gtk		# without gsx
#
Summary:	PostScript & PDF interpreter and renderer
Summary(de.UTF-8):	PostScript & PDF Interpreter und Renderer
Summary(fr.UTF-8):	Interpréteur et visualisateur PostScript & PDF
Summary(ja.UTF-8):	PostScript インタープリタ・レンダラー
Summary(pl.UTF-8):	Bezpłatny interpreter i renderer PostScriptu i PDF
Summary(tr.UTF-8):	PostScript & PDF yorumlayıcı ve gösterici
Name:		ghostscript
Version:	8.56
Release:	0.1
License:	GPL
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/ghostscript/%{name}-%{version}.tar.bz2
# Source0-md5:	498015a278308d147bea563be2c5165e
# we need to link with libjpeg recompiled with our parameters
Source2:	ftp://ftp.uu.net/graphics/jpeg/jpegsrc.v6b.tar.gz
# Source2-md5:	dbd5f3b47ed13132f04c685d608a7547
Source5:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source5-md5:	9b5953aa0cc155f4364f20036b848585
Patch0:		%{name}-missquotes.patch
Patch1:		%{name}-setuid.patch
Patch2:		%{name}-time_h.patch
Patch3:		%{name}-am.patch
# no device for cdj850 in non-espgs ghostscript
# look for patch in old spec for GNU ghostscript
#Patch4:		%{name}-gdevcd8-fixes.patch
#Patch5:		%{name}-glib.patch
Patch6:		%{name}-ijs_pkgconfig_64.patch
URL:		http://www.ghostscript.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-style-dsssl
BuildRequires:	glib2-devel
%{?with_system_jbig2dec:BuildRequires:	jbig2dec-devel}
# for gsx
%{?with_gtk:BuildRequires:	gtk+-devel}
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
# Required by 'gdevvglb' device.
%{?with_svga:BuildRequires:	svgalib-devel}
# for documentation regeneration
BuildRequires:	tetex
BuildRequires:	tetex-dvips
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXt-devel
Obsoletes:	ghostscript-afpl
Obsoletes:	ghostscript-gpl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Ghostscript は PostScript インタープリタです。ポストスクリプトと PDF
をレンダリングし、X window や他のプリンタフォーマットで出力
します。このパッケージは日本語対応しています。

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
Obsoletes:	ghostscript-afpl-gtk
Obsoletes:	ghostscript-gpl-gtk

%description gtk
Ghostscript with GTK+ console.

%description gtk -l pl.UTF-8
Ghostscript z konsolą GTK+.

%package devel
Summary:	libgs header files
Summary(pl.UTF-8):	Pliki nagłówkowe libgs
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	ghostscript-afpl-devel

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

%description ijs-static
Static libijs library.

%description ijs-static -l pl.UTF-8
Statyczna wersja biblioteki IJS.

%prep
%setup -q -a2
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1 -b .am
#%patch4 -p1
#%patch5 -p1
%patch6 -p1
ln -sf jp* jpeg

%build
# workarounds
touch ijs/ijs-config.1
%if %{with system_jbig2dec}
if [ -d jbig2dec ]; then
	rm -rf jbig2dec
fi
%endif
# not really needed with new patch :)
# sed -i -e 's#:$(gsdir)/fonts#:$(gsdir)/fonts:%{_datadir}/fonts:%{_datadir}/fonts/Type1#g' src/Makefile.in
#
%{__libtoolize}
cp -f %{_datadir}/automake/config.sub .
%{__aclocal}
%{__autoconf}
CFLAGS="%{rpmcflags} -DA4"
export CFLAGS
%configure \
	--with-fontpath="%{_datadir}/fonts:%{_datadir}/fonts/Type1" \
	--with-ijs \
	--with-jbig2dec \
	--with-jasper \
	--with-x

# NEEDS patch because no such configure options
#        --with-drivers=ALL%{?with_svga:,vgalib,lvga256} \

cd ijs
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-shared
cd ..

%{__make} \
	docdir=%{_docdir}/%{name}-%{version}

%{__make} so \
	docdir=%{_docdir}/%{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/ghostscript/lib,%{_libdir},%{_includedir}/ps}


%{__make} install \
	install_prefix=$RPM_BUILD_ROOT \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	datadir=$RPM_BUILD_ROOT%{_datadir} \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	docdir=$RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} \
	mandir=$RPM_BUILD_ROOT%{_mandir}


%{__make} soinstall \
	install_prefix=$RPM_BUILD_ROOT \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	datadir=$RPM_BUILD_ROOT%{_datadir} \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	docdir=$RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} \
	mandir=$RPM_BUILD_ROOT%{_mandir}

cd ijs
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
#	prefix=$RPM_BUILD_ROOT%{_prefix} \
#	bindir=$RPM_BUILD_ROOT%{_bindir} \
#	datadir=$RPM_BUILD_ROOT%{_datadir} \
#	libdir=$RPM_BUILD_ROOT%{_libdir} \
#	includedir=$RPM_BUILD_ROOT%{_includedir} \
#	mandir=$RPM_BUILD_ROOT%{_mandir}
cd ..

install lib/{gs_frsd,pdfopt,pdfwrite}.ps $RPM_BUILD_ROOT%{_datadir}/%{name}/lib

#install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/%{name}/lib
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/doc \
	$RPM_BUILD_ROOT%{_bindir}/*.sh \
	$RPM_BUILD_ROOT%{_mandir}/man1/{ps2pdf1{2,3},gsbj,gsdj,gsdj500,gslj,eps2eps}.1 \
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


bzip2 -dc %{SOURCE5} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

#mv -f $RPM_BUILD_ROOT%{_bindir}/{gsc,gs}
ln -sf gs $RPM_BUILD_ROOT%{_bindir}/gsc
ln -sf gs $RPM_BUILD_ROOT%{_bindir}/ghostscript

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}
%attr(755,root,root) %{_bindir}/[bdeflpsux]*
%attr(755,root,root) %{_bindir}/gs
%attr(755,root,root) %{_bindir}/wftopfa
%attr(755,root,root) %{_bindir}/gs[!x]*
%attr(755,root,root) %{_bindir}/ijs_*_example
%attr(755,root,root) %{_libdir}/libgs.so.*.*
%attr(755,root,root) %{_libdir}/libijs-*.so
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/lib
%{_datadir}/%{name}/lib/*.*
%dir %{_datadir}/%{name}/%{version}
%dir %{_datadir}/%{name}/%{version}/lib
# "*.*" will not match "Fontmap". It is OK.
%{_datadir}/%{name}/%{version}/lib/*.*
%{_datadir}/%{name}/%{version}/lib/[!F]*map
%{_datadir}/%{name}/%{version}/lib/FCOfontmap-PCLPS2
%config %verify(not md5 mtime size) %{_datadir}/%{name}/%{version}/lib/Fontmap
%{_datadir}/%{name}/%{version}/lib/pphs
%{_datadir}/%{name}/%{version}/Resource
%{_datadir}/%{name}/%{version}/examples
%{_mandir}/man*/*
%lang(cs) %{_mandir}/cs/man*/*
%lang(de) %{_mandir}/de/man*/*
%lang(es) %{_mandir}/es/man*/*
%lang(fr) %{_mandir}/fr/man*/*
%lang(pl) %{_mandir}/pl/man*/*

%if %{with gtk}
%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gsx
%endif

%files devel
%defattr(644,root,root,755)
%{_includedir}/ps
%attr(755,root,root) %{_libdir}/libgs.so

%files ijs-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ijs-config
%attr(755,root,root) %{_libdir}/libijs.so
%{_includedir}/ijs
%{_libdir}/libijs.la
%{_pkgconfigdir}/*.pc

%files ijs-static
%defattr(644,root,root,755)
%{_libdir}/libijs.a
