#
# Conditional build:
# _with_svgalib
#
Summary:	PostScript & PDF interpreter and renderer
Summary(de):	PostScript & PDF Interpreter und Renderer
Summary(fr):	Interpréteur et visualisateur PostScript & PDF
Summary(ja):	PostScript ¥¤¥ó¥¿¡¼¥×¥ê¥¿¡¦¥ì¥ó¥À¥é¡¼
Summary(pl):	Bezp³atny interpreter i renderer PostScriptu i PDF
Summary(tr):	PostScript & PDF yorumlayýcý ve gösterici
Name:		ghostscript
Version:	7.05
Release:	2
Vendor:		Aladdin Enterprises <bug-gs@aladdin.com>
License:	GPL
Group:		Applications/Graphics
Source0:	ftp://download.sourceforge.net/pub/sourceforge/ghostscript/%{name}-%{version}.tar.bz2
Source1:	http://www.ozemail.com.au/~geoffk/pdfencrypt/pdf_sec.ps
# we need to link with libjpeg recompiled with our parameters
Source2:	ftp://ftp.uu.net/graphics/jpeg/jpegsrc.v6b.tar.gz
Source3:	%{name}-find_devs.sh
Source5:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
Patch0:		%{name}-config.patch
Patch1:		%{name}-hpdj_driver.patch
Patch2:		%{name}-cdj880.patch
#Patch3:		%{name}-nosafer.patch
Patch4:		%{name}-missquotes.patch
Patch5:		%{name}-setuid.patch
Patch6:		%{name}-time_h.patch
URL:		http://www.ghostscript.com/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
# for gsx
BuildRequires:	gtk+-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libstdc++-devel
# Required by 'gdevvglb' device.
%ifarch %{ix86} alpha ppc
%{?_with_svgalib:BuildRequires:	svgalib-devel}
%endif
# for documentation regeneration
BuildRequires:	docbook-style-dsssl
BuildRequires:	/usr/bin/texi2html
BuildRequires:	tetex-dvips
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ghostscript is a PostScript interpreter. It can render both PostScript
and PDF compliant files to devices which include an X window, many
printer formats (including support for color printers), and popular
graphics file formats.

%description -l de
Ghostscipt ist ein PostScript-Interpretierer. Er kann sowohl
PostScript als auch PDF-konforme Dateien an Geräte ausgeben, zu denen
ein X-Fenster, viele Druckerformate (einschließlich Support für
Farbdrucker) und gängige Grafikdateiformate zählen.

%description -l fr
Ghostscript est un interpréteur PostScript. Il peut rendre des
fichiers PostScript ou PDF sur des périphériques dont une fenêtre X,de
nombreux types d'imprimantes (dont un support pour imprimantes
couleur), et des formats de fichiers graphiques populaires.

%description -l ja
Ghostscript ¤Ï PostScript ¥¤¥ó¥¿¡¼¥×¥ê¥¿¤Ç¤¹¡£¥Ý¥¹¥È¥¹¥¯¥ê¥×¥È¤È PDF
¤ò¥ì¥ó¥À¥ê¥ó¥°¤·¡¢X window ¤äÂ¾¤Î¥×¥ê¥ó¥¿¥Õ¥©¡¼¥Þ¥Ã¥È¤Ç½ÐÎÏ
¤·¤Þ¤¹¡£¤³¤Î¥Ñ¥Ã¥±¡¼¥¸¤ÏÆüËÜ¸ìÂÐ±þ¤·¤Æ¤¤¤Þ¤¹¡£

%description -l pl
Ghostcript jest interpreterem PostScriptu, jêzyka u¿ywanego do opisu
formatu dokumentu. Ghostscript potrafi przetworzyæ dokument w formacie
PostScript i PDF na szereg postaci wyj¶ciowych: drukarki (w³±czaj±c
kolorowe), okno X-Window i popularne formaty graficzne.

%description -l tr
GhostScript, PostScript ve PDF uyumlu dosyalarý, X penceresinde
gösterebilir ve birçok yazýcýnýn (renkli yazýcýlar dahil) basabileceði
biçime getirebilir.

%package gtk
Summary:	Ghostscript with Gtk+ console
Summary(pl):	Ghostscript z konsol± Gtk+
Group:		Applications/Graphics
Requires:	%{name} = %{version}

%description gtk
Ghostscript with Gtk+ console.

%description gtk -l pl
Ghostscript z konsol± Gtk+.

%package devel
Summary:	libgs header files
Summary(pl):	Pliki nag³ówkowe libgs
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for libgs - ghostscript shared library.

%description devel -l pl
Pliki nag³ówkowe libgs - wspó³dzielonej biblioteki ghostscript.

%package ijs-devel
Summary:	IJS development files
Summary(pl):	Pliki dla programistów IJS
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description ijs-devel
IJS development files.

%description ijs-devel -l pl
Pliki do tworzenia programów z u¿yciem biblioteki IJS.

%package ijs-static
Summary:	Static libijs
Summary(pl):	Statyczna biblioteka IJS
Group:		Development/Libraries
Requires:	%{name}-ijs-devel = %{version}

%description ijs-static
Static libijs.

%description ijs-static
Statyczna wersja biblioteki IJS.

%prep
%setup -q -a2
ln -sf src/unix-gcc.mak Makefile
%patch0 -p1
%patch1 -p1
%patch2 -p1
##%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
ln -sf jp* jpeg
install %{SOURCE3} .

%build
# NOTE: %%{SOURCE3} takes _blacklist_ as arguments, not the list of
# drivers to make!
%configure \
	--with-x \
	--with-ijs
cd ijs
%{__autoconf}
%configure
cd ..

%{__make} so \
	XCFLAGS="%{rpmcflags} -DA4=1 -w" \
	XLDFLAGS="%{rpmldflags}" \
	prefix=%{_prefix} \
	datadir=%{_datadir}/%{name} \
	mandir=%{_mandir} \
	docdir=%{_datadir}/doc/%{name}-%{version} \
	DEVICE_DEVS16="`/bin/sh %{SOURCE3} devs.mak \
%ifnarch %{ix86} alpha ppc
		vgalib lvga256\
%else
		%{!?_with_svgalib:vgalib lvga256} \
%endif
		`" \
	DEVICE_DEVS17="`/bin/sh %{SOURCE3} contrib.mak \
%ifnarch %{ix86} alpha ppc
		vgalib lvga256\
%else
		%{!?_with_svgalib:vgalib lvga256} \
%endif
		`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir},%{_libdir},%{_includedir}}

%{__make} soinstall \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	datadir=$RPM_BUILD_ROOT%{_datadir} \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}

cd ijs
%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	datadir=$RPM_BUILD_ROOT%{_datadir} \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	includedir=$RPM_BUILD_ROOT%{_includedir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}
cd ..

install lib/{gs_frsd,pdfopt,pdfwrite}.ps $RPM_BUILD_ROOT%{_datadir}/%{name}/lib

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/%{name}/lib
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/doc \
	$RPM_BUILD_ROOT%{_bindir}/*.sh \
	$RPM_BUILD_ROOT%{_mandir}/man1/{ps2pdf1{2,3},gsbj,gsdj,gsdj500,gslj,eps2eps}.1

echo ".so gs.1"     > $RPM_BUILD_ROOT%{_mandir}/man1/ghostscript.1
echo ".so ps2pdf.1" > $RPM_BUILD_ROOT%{_mandir}/man1/ps2pdf12.1
echo ".so ps2pdf.1" > $RPM_BUILD_ROOT%{_mandir}/man1/ps2pdf13.1
echo ".so ps2ps.1"  > $RPM_BUILD_ROOT%{_mandir}/man1/eps2eps.1
echo ".so gslp.1"   > $RPM_BUILD_ROOT%{_mandir}/man1/gsbj.1
echo ".so gslp.1"   > $RPM_BUILD_ROOT%{_mandir}/man1/gsdj.1
echo ".so gslp.1"   > $RPM_BUILD_ROOT%{_mandir}/man1/gsdj500.1
echo ".so gslp.1"   > $RPM_BUILD_ROOT%{_mandir}/man1/gslj.1

bzip2 -dc %{SOURCE5} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

mv -f $RPM_BUILD_ROOT%{_bindir}/{gsc,gs}
ln -sf gs $RPM_BUILD_ROOT%{_bindir}/gsc
ln -sf gs $RPM_BUILD_ROOT%{_bindir}/ghostscript

install -d $RPM_BUILD_ROOT%{_includedir}/ps
install src/{iapi,errors}.h $RPM_BUILD_ROOT%{_includedir}/ps

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/*.htm
%attr(755,root,root) %{_bindir}/[bdeflpsux]*
%attr(755,root,root) %{_bindir}/gs
%attr(755,root,root) %{_bindir}/gs[^x]*
%attr(755,root,root) %{_bindir}/ijs_client_example
%attr(755,root,root) %{_libdir}/libgs.so.*.*
%attr(755,root,root) %{_libdir}/libijs.so
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/lib
# "*.*" will not match "Fontmap". It is OK.
%{_datadir}/%{name}/lib/*.*
%dir %{_datadir}/%{name}/examples
%{_datadir}/%{name}/examples/*
%config %verify(not size md5 mtime) %{_datadir}/%{name}/lib/Fontmap
%{_mandir}/man*/*
%lang(cs) %{_mandir}/cs/man*/*
%lang(es) %{_mandir}/es/man*/*
%lang(fr) %{_mandir}/fr/man*/*
%lang(pl) %{_mandir}/pl/man*/*

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gsx

%files devel
%defattr(644,root,root,755)
%{_includedir}/ps
%{_libdir}/libgs.so

%files ijs-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ijs-config
%{_includedir}/ijs

%files ijs-static
%{_libdir}/libijs.a
